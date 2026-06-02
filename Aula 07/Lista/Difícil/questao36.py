n = int(input())
contador = 1
jogadas = []
pon1 = 0
pon2 = 0

while contador <= n:
    J1, J2 = input().split()
    jogada = {'J1' : J1, 'J2' : J2}
    jogadas.append(jogada)

    contador += 1
contador = 0

while contador < len(jogadas):
    J1 = jogadas[contador]['J1']
    J2 = jogadas[contador]['J2']

    if J1 == 'P':
        if J2 == 'S':
            pon2 += 1
            print(f'Rodada {contador + 1}: Jogador 2')
        elif J2 == 'T':
            pon1 += 1
            print(f'Rodada {contador + 1}: Jogador 1')
        elif J2 == 'P':
            print(f'Rodada {contador + 1}: Empate')
        else:
            print(f'Rodada {contador + 1}: Dados inválidos')
    elif J1 == 'T':
        if J2 == 'S':
            pon1 += 1
            print(f'Rodada {contador + 1}: Jogador 1')
        elif J2 == 'T':    
            print(f'Rodada {contador + 1}: Empate')
        elif J2 == 'P':
            pon2 += 1
            print(f'Rodada {contador + 1}: Jogador 2')
        else:
            print(f'Rodada {contador + 1}: Dados inválidos')
    elif J1 == 'S':
        if J2 == 'S':
            print(f'Rodada {contador + 1}: Empate')           
        elif J2 == 'T':
            pon2 += 1
            print(f'Rodada {contador + 1}: Jogador 2')
        elif J2 == 'P':
            pon1 += 1
            print(f'Rodada {contador + 1}: Jogador 1')
        else:
            print(f'Rodada {contador + 1}: Dados inválidos')
    else:
        print(f'Rodada {contador + 1}: Dados inválidos')

    contador += 1

if pon1 > pon2:
    print('Vitória do Jogador 1')
elif pon2 > pon1:
    print('Vitória do Jogador 2')
else:
    print('Empate')

