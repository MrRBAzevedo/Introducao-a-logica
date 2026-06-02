pares = 0
impares = 0

for i in iter(int, 1):
    numero = int(input())

    if numero < 0:
        print(f'{pares} números pares')
        print(f'{impares} números ímpares')
        break
    elif numero % 2 == 0:
        pares += 1
    else:
        impares += 1

