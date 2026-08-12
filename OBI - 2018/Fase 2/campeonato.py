X = list(map(int, input().split()))
rodada = 0
pos1 = X.index(1)
pos9 = X.index(9)
meio = 7.5

while True:
    if pos1 > meio and pos9 < meio or pos1 < meio and pos9 > meio:
        break
    elif pos1 > meio and pos9 > meio:
        meio += 2 ** (2 - rodada)
        rodada += 1
    elif pos1 < meio and pos9 < meio:
        meio -= 2 ** (2 - rodada)
        rodada += 1

if rodada == 0: print('final')
elif rodada == 1: print('semifinal')
elif rodada == 2: print('quartas')
else: print('oitavas')