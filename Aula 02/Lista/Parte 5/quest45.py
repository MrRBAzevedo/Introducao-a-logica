import subprocess
subprocess.run(['cls'], shell = True)

cel = float(input('Insira a temperatura em Celsius: '))
fah = cel * 9/5 + 32

print(f'A temperatura em Fahrenheit é: {fah:.1f}ºF')