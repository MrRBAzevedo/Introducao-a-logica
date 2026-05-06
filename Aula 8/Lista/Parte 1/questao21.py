n = int(input())
maior = 0

for i in range(n):
    nota = float(input())

    if nota > maior:
        maior = nota

print(maior)