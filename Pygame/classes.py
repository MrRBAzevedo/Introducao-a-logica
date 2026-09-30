import pygame

class Janela:
    def __init__(self, altura, largura, nome):
        self.janela = pygame.display.set_mode((altura, largura))
        pygame.display.set_caption(nome)
        self.cor = (0, 0, 0)
    
    def cor_fundo(self, red, green, blue):
        self.cor = (red, green, blue)

    def fundo(self):
        self.janela.fill(self.cor)