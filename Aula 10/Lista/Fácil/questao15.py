n = int(input())
valores = list(map(int, input().split()))
lista = []

for valor in valores:
    if valor not in lista:
        lista.append(valor)

for valor in lista:
    print(valor, end = ' ')