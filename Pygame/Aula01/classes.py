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

class Desenho:
    def __init__(self, janela):
        self.desenhando = False
        self.apagando = False
        self.tamanho = 10
        self.janela = janela
        self.tracado = []

    def Desenhar(self):
        for cor, posicao, raio in self.tracado:
            pygame.draw.circle(self.janela, cor, posicao, raio)

    def Desenhando(self):
        if self.desenhando:
            self.tracado.append(((0, 0, 0), pygame.mouse.get_pos(), self.tamanho))
        elif self.apagando:
            self.tracado.append(((255, 255, 255), pygame.mouse.get_pos(), self.tamanho))

    def Apagar(self):
        self.tracado.clear()


            