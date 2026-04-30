n = int(input())
num = 3
primos = [2]

while num <= n:
    div = 2

    while div < num:
        if num % div == 0:
            break

        div += 1
    else:
        primos.append(num)

    num += 1

contador = 0
fat = []
while n != 1:
    if n % primos[contador] == 0:
        n /= primos[contador]
        fat.append(primos[contador])
    else:
        contador += 1

print(max(fat))