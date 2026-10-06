import pygame

pygame.init()

loop_principal = True
fonte = pygame.font.SysFont("arial", 40, bold = True)
contador = 0
nome_jogador = ""
coletando_nome = True

tamanho_janela = (1600, 900)
janela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Janela do Jogo")


while coletando_nome:
    janela.fill((255, 255, 255))

    titulo = fonte.render("Digite seu nome e pressione Enter: ", True, (0, 0, 0))
    janela.blit(titulo, ((1600 - titulo.get_width()) // 2, 320))


    barra = "|" if pygame.time.get_ticks() % 1000 <= 500 else " "
    texto_nome = f'{nome_jogador}{barra}'
    nome = fonte.render(texto_nome, True, (0, 0, 0))
    janela.blit(nome, ((1600 - titulo.get_width()) // 2, 390))

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN and nome_jogador.strip():
                coletando_nome = False
            elif evento.key == pygame.K_BACKSPACE:
                nome_jogador = nome_jogador[:-1]
            else:
                nome_jogador += evento.unicode
    


while loop_principal:

    janela.fill((255, 255, 255))
    janela.blit(fonte.render(f"Contador: {contador}", True, (0, 0, 0)), (1300, 70))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop_principal = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                contador += 1


    pygame.display.flip()

pygame.quit()