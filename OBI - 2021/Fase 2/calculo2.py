s = int(input())
a = int(input())
b = int(input())
resultado = 0

while a <= b:
    num = str(a)
    soma = 0
    
    for i in range(len(num)):
        soma += int(num[i])

    if soma == s:
        resultado += 1

    a += 1

print(resultado)
