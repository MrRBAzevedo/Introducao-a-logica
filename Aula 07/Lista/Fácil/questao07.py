n = int(input())
contador = 1
pares = 0
impares = 0

while contador <= n:
    num = int(input())

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    contador += 1

print(f'Pares: {pares}')
print(f'Ímpares: {impares}')