n = int(input())
menor = 10

for i in range(n):
    nota = float(input())

    if nota < menor:
        menor = nota

print(menor)