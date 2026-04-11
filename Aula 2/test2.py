jogadas = []
num_jogadas = int(input())

for i in range(num_jogadas):
    a, b = map(int, input().split())
    div = min(a, b)

    while div > 0:
        if a % div == 0 and b % div == 0:
            jogadas.append(div)
            break

        div -= 1

for jogada in jogadas:
    print(jogada)

