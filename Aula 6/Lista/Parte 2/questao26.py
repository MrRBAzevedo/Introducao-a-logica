contador = 1

while contador <= 20:
    print(contador, end = ': ')
    print('par' if contador % 2 == 0 else 'ímpar')

    contador += 1