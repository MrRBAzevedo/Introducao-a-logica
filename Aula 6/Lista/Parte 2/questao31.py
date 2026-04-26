notas = []
aprovados = 0
reprovados = 0
recuperacao = 0
contador = 1

while contador <= 10:
    nota = float(input())

    if nota >= 7:
        aprovados += 1
    elif nota >= 5:
        recuperacao += 1
    else:
        reprovados += 1

    notas.append(nota)
    contador += 1

print(f'A média das notas é: {sum(notas) * 0.1}')
print(f'O número de alunos aprovados é: {aprovados}')
print(f'O número de alunos em recuperação é: {recuperacao}')
print(f'O número de alunos reprovados é: {reprovados}')