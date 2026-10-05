import pygame

loop_principal = True


tamanho_janela = (1600, 900)
janela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Janela do Jogo")


while loop_principal:



    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop_principal = False


    pygame.display.flip()

pygame.quit()