def Chutar(minimo, maximo):
    return (maximo - minimo) // 2 + minimo

import random

numero_jogadores = int(input('Digite o número de jogadores: '))
vez = 0
chute = 0
limite_inferior = 1
limite_superior = 1000000
numero = random.randint(limite_inferior, limite_superior) 
media = 0

while True:
    chute = Chutar(limite_inferior, limite_superior) 
    print(f'Jogador {vez + 1}, digite um número entre {limite_inferior} e {limite_superior}: {chute}')

    if chute == numero: break
    elif chute > numero: limite_superior = min(chute, limite_superior)
    else: limite_inferior = max(chute, limite_inferior)

    vez = (vez + 1) % numero_jogadores

print(f'Parabéns, jogador {vez + 1}! Você acertou o número {numero}')


