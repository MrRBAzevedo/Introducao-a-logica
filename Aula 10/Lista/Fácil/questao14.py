n = int(input())
valores = list(map(int, input().split()))

for i in range(n):
    if valores[i] % 2 == 0: valores[i] *= 2

for valor in valores:
    print(valor, end = ' ')