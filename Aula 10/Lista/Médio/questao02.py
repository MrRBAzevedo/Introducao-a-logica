n = int(input())
lista = list(map(int, input().split()))
maior = max(lista)
lista = [num for num in lista if num != maior]

if lista:
    print(max(lista))
else:
    print('NÃO EXISTE')
