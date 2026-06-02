n = int(input())
numeros = []

for i in range(n):
    numero = int(input())
    if numero == 0:
        numeros.pop()
    else:
        numeros.append(numero)

print(sum(numeros))