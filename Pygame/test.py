import pygame
import sys

pygame.init()

largura = 600
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Teste de Movimento")

# Posição do quadrado
x = 80
y = 180
velocidade = 2

cor_fundo = (30, 30, 30)
cor_quadrado = (58, 189, 141)

clock = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento automático
    y += velocidade

    if y > altura:
        y = -50

    # Desenho
    tela.fill(cor_fundo)
    pygame.draw.rect(tela, cor_quadrado, (x, y, 100, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()