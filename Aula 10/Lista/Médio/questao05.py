n = int(input())
lista = list(map(int, input().split()))
contador = 1

while contador < len(lista) - 1:
    if lista[contador] > lista[contador - 1] and lista[contador] > lista[contador + 1]:
        lista.pop(contador)
        contador -= 1
    else:
        contador += 1

print(lista)    