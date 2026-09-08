n, k = map(int, input().split())
lista = [int(numero) for numero in input().split()]
resultado = []
numeros = {}

for i in range(n):
    if lista[i] in numeros:
        if numeros[lista[i]] < k:
            resultado.append(lista[i])
            numeros[lista[i]] += 1
    else:
        resultado.append(lista[i])
        numeros[lista[i]] = 1

print(*resultado)