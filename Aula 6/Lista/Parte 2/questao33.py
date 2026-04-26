pares = 0
impares = 0
entrada = 1

while entrada != 0:
    entrada = int(input())

    if entrada % 2 == 0:
        pares += entrada
    else:
        impares += entrada

print(f'A soma dos números pares é: {pares}')
print(f'A soma dos números ímpares é: {impares}')