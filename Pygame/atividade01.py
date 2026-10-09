import pygame
from classes import Janela
import random

pygame.init()

janela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Renan é lindo")

loop_rodando = True
cor_fundo = (100, 0, 0)
contador_cliques = 0
posicao_circulo = False

while loop_rodando:

    janela.fill(cor_fundo)
    if posicao_circulo:
        pygame.draw.circle(janela, (255, 255, 255), posicao_circulo, 30)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            loop_rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            print(pygame.mouse.get_pos())
            # pygame.mouse.get_pos() retorna a posição do mouse
            contador_cliques += 1
            print(f'Cliques: {contador_cliques}')

            posicao_circulo = pygame.mouse.get_pos()

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            loop_rodando = False
    
    pygame.display.flip()

pygame.quit()