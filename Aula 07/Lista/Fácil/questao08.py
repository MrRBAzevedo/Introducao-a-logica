n = int(input())
contador = 1
numeros = []

while contador <= n:
    num = int(input())
    numeros.append(num)

    contador += 1

contador = 0
maior = numeros[0]
while contador < n:
    if numeros[contador] > maior:
        maior = numeros[contador]

    contador += 1

contador = 0
menor = numeros[0]
while contador < n:
    if numeros[contador] < menor:
        menor = numeros[contador]

    contador += 1

print(f'Maior: {maior}')
print(f'Menor: {menor}')