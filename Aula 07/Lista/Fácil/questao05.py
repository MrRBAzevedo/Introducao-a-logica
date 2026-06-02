n = int(input())
contador = 1
soma = 0

while contador <= n:
    nota = float(input())
    soma += nota
    contador += 1

print(f'{soma / n:.2f}')