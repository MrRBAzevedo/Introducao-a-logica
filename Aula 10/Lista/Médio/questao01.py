n = int(input())
lista = list(map(int, input().split()))
lista.sort()
contador = 1
maior = 0

for i in range(1, n):
    if lista[i] == lista[i - 1]:
        contador += 1
    else:
        contador = 1

    if contador > maior:
        maior = contador
        resultado = lista[i]

print(resultado)