# importa a biblioteca do pygame
import pygame
# importa as constantes e funções do pygame
from pygame.locals import *
# importa a função exit do sys, para fechar o jogo
from sys import exit

# inicia as funções do pygame
pygame.init()

# define a janela do jogo, uma variável com tamanho definido por uma tupla (x, y)
largura_tela = 1000
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))

# define uma string para ser exibida como nome da janela
pygame.display.set_caption('Pygame - Aula 1')

# loop principal do jogo
while True:

    # loop for que detecta os eventos, como as entradas
    for event in pygame.event.get():

        # condição que desencadeia o fim do jogo ao fechamento da janela
        if event.type == QUIT:
            pygame.quit()
            exit()

    # atualiza a janela do jogo, necessário para visualizar as mudanças
    pygame.display.update()

