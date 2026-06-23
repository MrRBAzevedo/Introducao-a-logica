n = int(input())
valores = list(map(int, input().split()))
lista = []
soma = 0

for valor in valores:
    soma += valor
    lista.append(soma)

for valor in lista:
    print(valor, end = ' ')
