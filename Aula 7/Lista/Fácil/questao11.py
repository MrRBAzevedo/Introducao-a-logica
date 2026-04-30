num = list(input())
contador = 0
soma = 0

while contador < len(num):
    soma += int(num[contador])
    contador += 1

print(soma)