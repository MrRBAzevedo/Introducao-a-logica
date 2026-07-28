s = int(input())
a = int(input())
b = int(input())
resultado = 0

while a <= b:
    num = str(a)
    soma = int(num[0]) + int(num[1])

    if soma == s:
        resultado += 1

    a += 1

print(resultado)
