import pygame
from classes import Janela

pygame.init()

janela = Janela(1600, 900, 'Atividade 01')

loop_rodando = True

while loop_rodando:

    janela.fundo()


    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            loop_rodando = False

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_m:
            janela.cor_fundo(255, 0, 255)

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_y:
            janela.cor_fundo(255, 255, 0)
        
    pygame.display.flip()

pygame.quit()