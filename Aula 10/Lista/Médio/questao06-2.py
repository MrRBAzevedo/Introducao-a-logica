n, k = map(int, input().split())
lista = list(map(int, input().split()))
resultado = []
ocorrencias = {}

for i, valor in enumerate(lista):
    if valor in ocorrencias:
        ocorrencias[valor] += 1
    else:
        ocorrencias[valor] = 1

    if ocorrencias[valor] <= k:
        resultado.append(valor)

print(*resultado)