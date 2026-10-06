import pygame
from Pygame.Aula01.classes import Desenho

tamanho_janela = (1600, 900)
cor_fundo = (255, 255, 255)
loop_rodando = True

janela = pygame.display.set_mode((tamanho_janela))
pygame.display.set_caption("Janela do Jogo")

desenho = Desenho(janela)

while loop_rodando:
    janela.fill(cor_fundo)
    desenho.Desenhando()
    desenho.Desenhar()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop_rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                loop_rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                desenho.desenhando = True
            elif evento.button == 3:
                desenho.apagando = True

        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                desenho.desenhando = False
            elif evento.button == 3:
                desenho.apagando = False


    pygame.display.flip()

pygame.quit()