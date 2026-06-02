soma_positivos = 0
soma_negativos = 0
contador = 1
limite = int(input())

while contador <= limite:
    num = float(input())

    if num > 0:
        soma_positivos += num
    else:
        soma_negativos += num

    contador += 1

print(f'Soma dos positivos: {soma_positivos}')
print(f'Soma dos negativos: {soma_negativos}')