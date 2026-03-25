import subprocess
subprocess.run(['cls'], shell = True)
 
valor = float(input('Insira o valor do produto: '))
desc = float(input('Insira o percentual do desconto: '))
valor *= (100 - desc) / 100

print(f'O valor após o desconto é: R$ {valor:.2f}')