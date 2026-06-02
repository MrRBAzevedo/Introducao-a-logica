from quest31 import media
notas = []
aprovados = 0
reprovados = 0
em_recuperacao = 0

for i in range(10):
    nota = float(input())
    notas.append(nota)

for nota in notas:
    if nota >= 7:
        aprovados += 1
    elif nota >= 5:
        em_recuperacao += 1
    else:
        reprovados += 1

print(f'A média das notas: {media(notas)}')
print(f'Número de alunos aprovados: {aprovados}')
print(f'Número de alunos em recuperação: {em_recuperacao}')
print(f'Número de alunos reprovados: {reprovados}')

