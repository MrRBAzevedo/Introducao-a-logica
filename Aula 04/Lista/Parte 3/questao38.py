num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))
operador = input('Insira o operador: ')

if operador == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif operador == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif operador == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif operador == '/':
    if num2 == 0:
        print('Não existe divisão por zero')
    else:
        print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('Operador inválido')