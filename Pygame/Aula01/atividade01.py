import pygame

pygame.init()

tamanho_janela = (1600, 900)
janela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Janela do Jogo")

cor_fundo = (255, 255, 255)
fonte = pygame.font.SysFont("arial", 40, bold = True)
texto_inicial = fonte.render("Olá, Pygame!", True, (0, 0, 0))
tem_texto = True

loop_rodando = True
desenhado = []
desenhar = False
apagar = False
tamanho = 20


while loop_rodando:
    janela.fill(cor_fundo)

    if tem_texto:
        janela.blit(texto_inicial, (800, 450))

    

    pygame.draw.rect(janela, (100, 100, 100), (1400, 800, 100, 50), 100, 10)
    pygame.draw.rect(janela, (100, 100, 100), (1200, 800, 100, 50), 100, 10)
    pygame.draw.rect(janela, (100, 100, 100), (1000, 800, 100, 50), 100, 10)

    if apagar:
        desenhado.append((pygame.mouse.get_pos(), (255, 255, 255), tamanho))

    if desenhar:
        desenhado.append((pygame.mouse.get_pos(), (0, 0, 0), tamanho))

    for posicao, cor, raio in desenhado:
        if 980 < posicao[0] < 1600 and 810 < posicao[1] < 860:
            pass
        else:
            pygame.draw.circle(janela, cor, posicao, raio)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            loop_rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                loop_rodando = False

            if evento.key == pygame.K_l:
                desenhado.clear()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                tem_texto = False
                posicao = pygame.mouse.get_pos()
                if 1400 < posicao[0] < 1500 and 800 < posicao[1] < 850:
                    desenhado.clear()
                elif 1200 < posicao[0] < 1300 and 800 < posicao[1] < 850:
                    tamanho += 10
                elif 1000 < posicao[0] < 1100 and 800 < posicao[1] < 850:
                    if tamanho > 10:
                        tamanho -= 10                                                
                else:
                    desenhar = True
            if evento.button == 3:
                apagar = True

        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                desenhar = False
            if evento.button == 3:
                apagar = False
        
    pygame.display.flip()

pygame.quit()