pares = 0
impares = 0
entrada = 1

while entrada > 0:
    entrada = int(input())

    if entrada > 0:
        if entrada % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f'A quantidade de números pares é: {pares}')
print(f'A quantidade de números ímpares é: {impares}')