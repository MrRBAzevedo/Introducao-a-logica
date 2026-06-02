n = int(input())
contador = 1

while contador <= n:
    if contador % 2 == 0 and contador % 7 == 0:
        print(contador)

    contador += 1
    