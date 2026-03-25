import subprocess
subprocess.run(['cls'], shell = True)

preco = float(input('Preço: '))
unidade = int(input('Unidades: '))
valor_total = preco * unidade

print(f'O valor total da compra foi: {valor_total:.2f}')