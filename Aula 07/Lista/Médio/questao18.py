a = int(input())
b = int(input())
contador = 0
mmc = []
num = 3
primos = [2]

while num <= max(a, b):
    div = 2

    while div < num:
        if num % div == 0:
            break

        div += 1
    else:
        primos.append(num)

    num += 1

while a and b != 1:
    if a % primos[contador] == 0 and b % primos[contador] == 0:
        mmc.append(primos[contador])
        a /= primos[contador]
        b /= primos[contador]
    elif a % primos[contador] == 0:
        mmc.append(primos[contador])
        a /= primos[contador]
    elif b % primos[contador] == 0:
        mmc.append(primos[contador])
        b /= primos[contador]
    else:
        contador += 1

prod = 1
contador = 0
while contador < len(mmc):
    prod *= mmc[contador]
    contador += 1

print(prod)