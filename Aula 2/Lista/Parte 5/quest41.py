import subprocess
subprocess.run(['cls'], shell = True)

aluno = input('Insira o nome do aluno: ')
n1, n2, n3 = map(float, input('Insira as notas: ').split())

media = (n1 + n2 + n3) / 3

print(f'Aluno: {aluno}')
print(f'Média: {media:.1f}')