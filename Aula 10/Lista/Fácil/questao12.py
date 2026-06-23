n = int(input())
valores = list(map(int, input().split()))

for i in range(n):
    valores[i] *= -1

for valor in valores:
    print(valor, end = ' ')