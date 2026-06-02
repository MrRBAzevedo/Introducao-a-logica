a = int(input())
b = int(input())
primos = []
limite = max(a, b)
primo = min(a, b)

while primo <= limite:
    div = 2
    while div < primo:
        if primo % div == 0:
            break

        div += 1
    else:
        if primo != 1: primos.append(primo)

    primo += 1

print(primos)