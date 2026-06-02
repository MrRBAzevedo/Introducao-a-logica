sal = float(input('Insira o salário: '))

print(f'O imposto será R$ {sal * 0.15:.2f}' if sal > 3000 else f'O imposto será R$ {sal * 0.075:.2f}')