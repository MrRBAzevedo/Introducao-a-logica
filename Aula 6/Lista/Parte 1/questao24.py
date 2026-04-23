contador = 0
soma = 0
num = list(input())

while contador < len(num):
    soma += int(num[contador])
    contador += 1

print(soma)