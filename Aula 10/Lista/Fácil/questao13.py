n = int(input())
valores = list(map(int, input().split()))

for i in range(n):
    if valores[i] < 0: valores[i] = 0

for valor in valores:
    print(valor, end = ' ')