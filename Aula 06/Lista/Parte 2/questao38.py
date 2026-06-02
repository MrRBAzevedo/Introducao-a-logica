n = int(input())
contador = 1
numeros = []

while contador <= n:
    num = int(input())
    numeros.append(num)

    contador += 1

print(f'O maior dos números é: {max(numeros)}')
print(f'O menor dos números é: {min(numeros)}')
