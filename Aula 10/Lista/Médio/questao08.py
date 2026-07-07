n, soma = map(int, input().split())
lista = list(map(int, input().split()))
elementos = {}

for i, valor in enumerate(lista):
    par = soma - valor

    if par in elementos:
        print(elementos[par], i)
        break

    elementos[valor] = i

