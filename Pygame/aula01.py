import pygame
# Importa a biblioteca do Pygame para o código
from classes import Janela

pygame.init()
# Inicia os módulos do Pygame

janela_principal = Janela(1600, 900, 'Janela principal')

# janela = pygame.display.set_mode((1600, 900))
# Abre a janela do jogo
# pygame.display.set_caption("Janela de Pygame")
# Modifica o título da janela

corFundo = [0, 0, 0]

loop_rodando = True

while loop_rodando:
    # É o loop principal do jogo, responsável por manter a janela aberta e processar os eventos causados pelo usuário

    # janela.fill(corFundo)
    # Preenche o fundo da janela com uma cor sólida
    # Deve ser chamada a cada frame

    for evento in pygame.event.get():
        # pygame.event.get retorna a lista de eventos que aconteceram desde a última iteração, como comandos do usuário

        if evento.type == pygame.QUIT:
            # evento.type retorna o tipo do evento
            # Nesse caso, o código do laço IF será executado quando o evento for do tipo QUIT, isto é, o fechamento da janela

            loop_rodando = False
            # Torna a condição para a iteração do loop falsa, fazendo com que não seja executado novamente

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 2:
            # O evento do tipo pygame.MOUSEBUTTONDOWN correponde ao pressionamento de qualquer botão do mouse
            # Para saber qual o botão específico, utiliza-se o método evento.button, que retorna 1 (esquero), 2 (scroll) ou 3 (direito)
            
            loop_rodando = False

    pygame.display.flip()
    # Atualiza o conteúdo da janela
    # Deve ser chamado em toda iteração do loop princiopal


pygame.quit()
# Finaliza os módulos do Pygame, encerrando o código.


