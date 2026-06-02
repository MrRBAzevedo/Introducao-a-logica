import subprocess
subprocess.run(['cls'], shell = True)

raio = float(input('Insira o raio: '))
area = 3.14159 * raio ** 2

print(f'A área do círculo é: {area:.2f}')