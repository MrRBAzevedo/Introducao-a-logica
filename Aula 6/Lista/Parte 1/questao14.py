base = int(input())
expoente = int(input())
contador = 1
resultado = 1

while contador <= expoente:
    resultado *= base
    contador += 1

print(resultado)
