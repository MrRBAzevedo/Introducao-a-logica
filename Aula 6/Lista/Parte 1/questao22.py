contador = 1
notas = []
n = int(input())

while contador <= n:
    nota = int(input())
    notas.append(nota)
    contador += 1

print(min(notas))
