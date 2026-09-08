n, k = map(int, input().split())
lista = [int(numero) for numero in input().split()]
resultado = []
numeros = {}

for i in range(n):
    numeros[lista[i]] = 0

for i in range(n):
    if numeros[lista[i]] < k:
        resultado.append(lista[i])
        numeros[lista[i]] += 1


print(*resultado)