n = int(input('Número de valores a serem lidos: '))
lista = []

for i in range(n):
    valor = int(input())
    lista.append(valor)

soma = 0

for valor in lista:
    soma += valor

print(soma)

for i in range(len(lista)):
    valor = lista[i]