positivos = 0
negativos = 0
nulos = 0
contador = 1

while contador <= 10:
    entrada = int(input())

    if entrada > 0:
        positivos += 1
    elif entrada < 0:
        negativos += 1
    else:
        nulos += 1

    contador += 1

print(f'''{positivos} números maiores que zero
{negativos} números menores que zero
{nulos} números iguais a zero
''')