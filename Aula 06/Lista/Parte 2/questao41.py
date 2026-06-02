contador = 1
limite = int(input())
pares = []

while contador <= limite:
    a, b = map(int, input().split())

    if a > b:
        pares.append((a, b))
    elif a < b:
        pares.append((b, a))
    else:
        pares.append('Iguais')

    contador += 1


contador = 0
while contador < limite:
    if pares[contador] == 'Iguais':
        print('Os números são iguais')
    else:
        print(f'O maior dos números é {pares[contador][0]} e o menor é {pares[contador][1]}' )

    contador += 1