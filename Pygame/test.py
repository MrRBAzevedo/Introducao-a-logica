#!/usr/bin/env python3
"""
TERMO em Pygame
---------------
Adivinhe a palavra de 5 letras em 6 tentativas.
  Verde    = letra certa no lugar certo
  Amarelo  = letra existe, mas em outra posição
  Cinza    = letra não existe na palavra

Controles:
  Letras do teclado (ou clique no teclado da tela) ... digitar
  Backspace ................................ apagar
  Enter .................................... enviar palpite / novo jogo (ao final)
  Esc ...................................... sair

Requisitos: pip install pygame
Opcional: coloque um arquivo "palavras.txt" (uma palavra por linha) ao lado deste
script para ampliar o dicionário de palavras válidas e sorteáveis.
"""

import math
import os
import random
import sys
import time
import unicodedata
from collections import Counter

import pygame

# ----------------------------------------------------------------------------
# Configurações
# ----------------------------------------------------------------------------
WORD_LEN = 5
MAX_TRIES = 6

# Se True, só aceita palpites que estejam na lista de palavras.
# Se False, aceita qualquer combinação de 5 letras (mais tranquilo com a lista embutida).
STRICT_DICTIONARY = False

WIDTH, HEIGHT = 620, 800
FPS = 60

# Cores (inspiradas no Termo original)
C_BG = (24, 22, 24)
C_TILE_EMPTY = (49, 42, 44)
C_TILE_BORDER = (86, 74, 78)
C_TILE_ACTIVE = (200, 190, 194)
C_CORRECT = (58, 163, 148)
C_PRESENT = (211, 173, 105)
C_ABSENT = (68, 58, 61)
C_KEY = (110, 92, 98)
C_TEXT = (240, 236, 238)
C_DIM = (150, 138, 143)
C_TOAST_BG = (240, 236, 238)
C_TOAST_TEXT = (24, 22, 24)

STATE_COLOR = {"correct": C_CORRECT, "present": C_PRESENT, "absent": C_ABSENT}
STATE_RANK = {"absent": 1, "present": 2, "correct": 3}

FLIP_DURATION = 0.45
FLIP_STAGGER = 0.25

# ----------------------------------------------------------------------------
# Palavras
# ----------------------------------------------------------------------------
BASE_WORDS = """
abrir acento afeto agudo ainda aluno amigo amora anexo antes apito areia arroz
astro atraso aviso azeite bagaço baixo balde banco barco barro beijo berço bicho
birra bolsa brasa brisa bruma burro busca cabra cacho calma campo canto carro
casal causa cinto cinza clima cobra coisa colar comum corpo corda corte couro
credo cruel culto curso dados dança dente desde dizer doçura dorso drama ducha
dueto ebano efeito ensino entre época errar essas exame extra fabula faixa falso
festa fibra ficar fiéis fogão folha fonte forma forno fraco frase freio frevo
fruto fundo furto gamba ganho garfo gemer gente girar gosto grama grito grupo
guarda gênio hábil herói honra hoje humor ideia igual ilha inveja jarro jeito
jogar jovem julho justo juros lábio lance largo laudo lazer leite lenda letra
levar limão limpo linda lição livro lixão local longe louco lugar luxo lúcido
macio magia maior mamão manha manto marca massa matar mesmo metal meiga mexer
milho minha moeda molho monte morar morte mosca motor mudar mundo mural nação
nasce navio negro nervo neve ninho noite norte nossa nível obter ódio ombro
ondas opção ordem orgão osso ótimo outro ouvir padre pagar paixão palco pausa
pedra peixe pente perda pilha pinto plano plena poder poção ponto porta posse
pouco praça prata prazo preto preço prova pular punho quase queda quero quilo
rabos rádio raiva ramos rapaz razão regra reino relva rende resto rever rico
rimar risco ritmo rocha rosto rumor sabor sacola saída salto samba sangue santo
saúde selva senso serra série sexta sinal sitio sobre sogro solda som sonho
sorte suave subir sujar super tarde tempo tenda terra tigre tinta tirar tocar
todos tosse touro trago trama trigo troca trono tudo turma união único urgir
usina vacas vagão valer valor vapor vazio velho vento verde verso vício vidro
vigor vinho viver volta vulto xeque zebra zelar zombar
afago agito alma amplo anjo apoio arena aroma arte asilo atlas atual audaz
autor avião bater bravo breve brilho caixa calor canoa cheio chuva ciúme claro
cheiro corar cravo curva danar deixa denso depor deste dever dobra doido dotar
duplo durar elite emoção enfim ensaio erro etapa fator feliz ferro fiapo firme
fixar flora fluir folga força forte fosco fresco fugir fumar fusão gancho gasto
gelar geral glória grato grave gripe habil haste helio hino idade idoso ileso
imune ideal joias juizo karma laço leão lento levar lousa lugar lutar maçã
magro mania mapas marco mecha medir meiga melão mente meses metro mínimo mirar
moral morno mover muito museu nadar nariz nobre nomes novos nuvem obras oeste
ontem opaco ouro pacto pajem palma panela papel parar parte passo pátio pedir
pegar pelos penal perto pesar piano pisar placa pluma polir pomba porco pouso
prato prime prosa puxar quota rango rasgo reais reata rezar riste rival rolar
rugir sabão sagaz salão sábio secar sedar segue selar senha serio sigla sinto
sobra sofá sopro suar sumir tabua talvez tanto tapar tecer tenso terno texto
tímido tinto tolos tomar torre total trair trato trevo tribo troco turno útil
vaga vasto vejam venda vespa vetar viola virar visão visto vital vogal vozes
""".split()


def norm(s: str) -> str:
    """Remove acentos e coloca em maiúsculas (para comparar palavras)."""
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").upper()


def load_words():
    """Retorna (lista de respostas com acento, conjunto de palpites válidos)."""
    words = list(BASE_WORDS)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "palavras.txt")
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                words += [w.strip().lower() for w in f if w.strip()]
        except OSError:
            pass

    answers, seen = [], set()
    for w in words:
        w = w.strip().lower()
        n = norm(w)
        if len(n) == WORD_LEN and n.isalpha() and n.isascii() and n not in seen:
            seen.add(n)
            answers.append(w)
    return answers, seen


# ----------------------------------------------------------------------------
# Lógica
# ----------------------------------------------------------------------------
def evaluate(guess: str, answer: str):
    """Devolve lista de estados ('correct', 'present', 'absent') por letra."""
    states = ["absent"] * WORD_LEN
    remaining = Counter()
    for i in range(WORD_LEN):
        if guess[i] == answer[i]:
            states[i] = "correct"
        else:
            remaining[answer[i]] += 1
    for i in range(WORD_LEN):
        if states[i] == "absent" and remaining[guess[i]] > 0:
            states[i] = "present"
            remaining[guess[i]] -= 1
    return states


class Game:
    def __init__(self, answers, valid):
        self.answers = answers
        self.valid = valid
        self.reset()

    def reset(self):
        self.answer_display = random.choice(self.answers)
        self.answer = norm(self.answer_display)
        self.rows = []  # cada item: {"word", "states", "start"}
        self.current = ""
        self.status = "playing"  # playing | revealing | won | lost
        self.pending_status = "playing"
        self.reveal_end = None
        self.key_states = {}
        self.toast = ""
        self.toast_until = 0.0
        self.shake_until = 0.0

    # -- mensagens ----------------------------------------------------------
    def show_toast(self, text, seconds=1.6):
        self.toast = text
        self.toast_until = time.time() + seconds

    # -- entrada ------------------------------------------------------------
    def type_letter(self, ch):
        if self.status == "playing" and len(self.current) < WORD_LEN:
            self.current += ch

    def backspace(self):
        if self.status == "playing":
            self.current = self.current[:-1]

    def submit(self):
        if self.status in ("won", "lost"):
            self.reset()
            return
        if self.status != "playing":
            return
        if len(self.current) < WORD_LEN:
            self.show_toast("Só palavras com 5 letras")
            self.shake_until = time.time() + 0.5
            return
        if STRICT_DICTIONARY and self.current not in self.valid:
            self.show_toast("Essa palavra não é aceita")
            self.shake_until = time.time() + 0.5
            return

        states = evaluate(self.current, self.answer)
        now = time.time()
        self.rows.append({"word": self.current, "states": states, "start": now})
        won = self.current == self.answer
        self.current = ""
        self.status = "revealing"
        self.pending_status = (
            "won" if won else ("lost" if len(self.rows) >= MAX_TRIES else "playing")
        )
        self.reveal_end = now + FLIP_STAGGER * (WORD_LEN - 1) + FLIP_DURATION

    # -- atualização --------------------------------------------------------
    def update(self):
        if self.status == "revealing" and time.time() >= self.reveal_end:
            row = self.rows[-1]
            for ch, st in zip(row["word"], row["states"]):
                old = self.key_states.get(ch)
                if old is None or STATE_RANK[st] > STATE_RANK[old]:
                    self.key_states[ch] = st
            self.status = self.pending_status
            if self.status == "won":
                msgs = ["Genial!", "Magnífico!", "Impressionante!", "Espetacular!",
                        "Muito bom!", "Ufa, foi por pouco!"]
                self.toast = msgs[len(self.rows) - 1]
            elif self.status == "lost":
                self.toast = f"A palavra era {self.answer_display.upper()}"
            self.toast_until = float("inf") if self.status in ("won", "lost") else 0


# ----------------------------------------------------------------------------
# Interface
# ----------------------------------------------------------------------------
TILE = 64
GAP = 8
GRID_W = WORD_LEN * TILE + (WORD_LEN - 1) * GAP
GRID_X = (WIDTH - GRID_W) // 2
GRID_Y = 110

KEY_W, KEY_H, KEY_GAP = 48, 58, 6
KB_Y = 596
KB_ROWS = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]


def build_keyboard():
    """Cria a lista de teclas: (rótulo, Rect)."""
    keys = []
    for r, row in enumerate(KB_ROWS):
        y = KB_Y + r * (KEY_H + KEY_GAP)
        items = [(c, KEY_W) for c in row]
        if r == 2:
            items = [("ENTER", 78)] + items + [("⌫", 78)]
        total = sum(w for _, w in items) + KEY_GAP * (len(items) - 1)
        x = (WIDTH - total) // 2
        for label, w in items:
            keys.append((label, pygame.Rect(x, y, w, KEY_H)))
            x += w + KEY_GAP
    return keys


def draw_tile(surf, font, rect, letter, fill, border=None, scale_y=1.0):
    if scale_y <= 0.02:
        return
    h = max(2, int(rect.height * scale_y))
    r = pygame.Rect(rect.x, rect.centery - h // 2, rect.width, h)
    pygame.draw.rect(surf, fill, r, border_radius=6)
    if border:
        pygame.draw.rect(surf, border, r, width=2, border_radius=6)
    if letter and scale_y > 0.35:
        txt = font.render(letter, True, C_TEXT)
        surf.blit(txt, txt.get_rect(center=r.center))


def draw_grid(surf, font, game):
    now = time.time()
    shake = 0
    if now < game.shake_until:
        left = game.shake_until - now
        shake = int(math.sin(now * 60) * 8 * min(1.0, left / 0.5))

    for r in range(MAX_TRIES):
        for c in range(WORD_LEN):
            rect = pygame.Rect(
                GRID_X + c * (TILE + GAP),
                GRID_Y + r * (TILE + GAP),
                TILE,
                TILE,
            )
            if r < len(game.rows):  # linha já enviada
                row = game.rows[r]
                p = (now - row["start"] - c * FLIP_STAGGER) / FLIP_DURATION
                letter = row["word"][c]
                if p < 0:
                    draw_tile(surf, font, rect, letter, C_TILE_EMPTY, C_TILE_BORDER)
                elif p < 0.5:
                    draw_tile(surf, font, rect, letter, C_TILE_EMPTY,
                              C_TILE_BORDER, 1 - 2 * p)
                elif p < 1:
                    draw_tile(surf, font, rect, letter,
                              STATE_COLOR[row["states"][c]], None, 2 * p - 1)
                else:
                    draw_tile(surf, font, rect, letter, STATE_COLOR[row["states"][c]])
            elif r == len(game.rows) and game.status == "playing":  # linha ativa
                rect.x += shake
                if c < len(game.current):
                    draw_tile(surf, font, rect, game.current[c],
                              C_TILE_EMPTY, C_TILE_ACTIVE)
                elif c == len(game.current):
                    draw_tile(surf, font, rect, "", C_TILE_EMPTY, C_TILE_ACTIVE)
                else:
                    draw_tile(surf, font, rect, "", C_TILE_EMPTY, C_TILE_BORDER)
            else:
                draw_tile(surf, font, rect, "", C_TILE_EMPTY, C_TILE_BORDER)


def draw_keyboard(surf, font, keys, game):
    for label, rect in keys:
        st = game.key_states.get(label)
        color = STATE_COLOR[st] if st else C_KEY
        pygame.draw.rect(surf, color, rect, border_radius=6)
        txt = font.render(label, True, C_TEXT)
        surf.blit(txt, txt.get_rect(center=rect.center))


def draw_toast(surf, font, hint_font, game):
    now = time.time()
    if not game.toast or now >= game.toast_until:
        return
    txt = font.render(game.toast, True, C_TOAST_TEXT)
    box = txt.get_rect()
    box.inflate_ip(36, 20)
    box.center = (WIDTH // 2, 556)
    pygame.draw.rect(surf, C_TOAST_BG, box, border_radius=8)
    surf.blit(txt, txt.get_rect(center=box.center))
    if game.status in ("won", "lost"):
        hint = hint_font.render("Pressione ENTER para jogar de novo", True, C_DIM)
        surf.blit(hint, hint.get_rect(center=(WIDTH // 2, 585)))


def main():
    pygame.init()
    pygame.display.set_caption("TERMO — Pygame")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("arial", 46, bold=True)
    tile_font = pygame.font.SysFont("arial", 38, bold=True)
    key_font = pygame.font.SysFont("arial", 20, bold=True)
    toast_font = pygame.font.SysFont("arial", 22, bold=True)
    hint_font = pygame.font.SysFont("arial", 16)

    answers, valid = load_words()
    game = Game(answers, valid)
    keys = build_keyboard()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    game.submit()
                elif event.key == pygame.K_BACKSPACE:
                    game.backspace()
                else:
                    ch = norm(event.unicode) if event.unicode else ""
                    if len(ch) == 1 and "A" <= ch <= "Z":
                        game.type_letter(ch)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for label, rect in keys:
                    if rect.collidepoint(event.pos):
                        if label == "ENTER":
                            game.submit()
                        elif label == "⌫":
                            game.backspace()
                        else:
                            game.type_letter(label)
                        break

        game.update()

        screen.fill(C_BG)
        title = title_font.render("TERMO", True, C_TEXT)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 55)))
        sub = hint_font.render(
            f"Tentativa {min(len(game.rows) + (1 if game.status == 'playing' else 0), MAX_TRIES)}"
            f" de {MAX_TRIES}",
            True, C_DIM,
        )
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, 90)))

        draw_grid(screen, tile_font, game)
        draw_keyboard(screen, key_font, keys, game)
        draw_toast(screen, toast_font, hint_font, game)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()