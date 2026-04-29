n = int(input())
contador = 1
numeros = []

while contador <= n:
    num = int(input())
    numeros.append(num)

    contador += 1

contador = 1
maior = numeros[0]
while contador < n:
    if numeros[contador] > numeros[contador - 1]:
        maior = numeros[contador]

    contador += 1

contador = 1
menor = numeros[0]
while contador < n:
    if numeros[contador] < numeros[contador - 1]:
        menor = numeros[contador]

    contador += 1

print(f'Maior: {maior}')
print(f'Menor: {menor}')