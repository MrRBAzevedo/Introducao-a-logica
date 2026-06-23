na = int(input())
a = list(map(int, input().split()))
nb = int(input())
b = list(map(int, input().split()))
lista = []

for valor in a:
    if valor not in b: lista.append(valor)

if len(lista) == 0:
    print('VAZIA')
else: 
    for valor in lista:
        print(valor, end = ' ')