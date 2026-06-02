Podovan = [1, 1, 1]
limite = int(input())
contador = 3

while contador < limite:
    num = Podovan[contador - 2] + Podovan[contador - 3]
    Podovan.append(num)

    contador += 1

for num in Podovan:
    print(num, end = ' ')