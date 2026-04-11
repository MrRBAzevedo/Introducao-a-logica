import subprocess
subprocess.run('cls', shell = 'True')

nota = float(input('Insira a nota: '))

if nota >= 9:
    print(f'A nota {nota} corresponde ao conceito A')
elif nota >= 7:
    print(f'A nota {nota} corresponde ao conceito B')
elif nota >= 5:
    print(f'A nota {nota} corresponde ao conceito C')
else:
    print(f'A nota {nota} corresponde ao conceito D')