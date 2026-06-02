n = int(input())
contador = 1
fatorial = 1

while contador <= n:
    fatorial *= contador
    contador += 1

print(fatorial)