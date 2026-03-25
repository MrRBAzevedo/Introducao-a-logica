import subprocess
subprocess.run(['cls'], shell = True)

x = int(input('Insira um número: '))
y = int(input('Insira outro número: '))

print(f'\nA soma de {x} e {y} é {x + y}')
print(f'A diferença entre {x} e {y} é {x - y}')
print(f'O produto de {x} e {y} é {x * y}')
print(f'A razão de {x} e {y} é {x / y:.2f}')
