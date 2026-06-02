num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
operacao = int(input('Insira a operação: '))

if operacao == 1:
    print(f'O maior valor é {max(num1, num2)}')
elif operacao == 2:
    print(f'O menor valor é {min(num1, num2)}')
elif operacao == 3:
    print(f'A soma de {num1} e {num2} é {num1 + num2}')
elif operacao == 4:
    print(f'A diferença entre {num1} e {num2} é {num1 - num2}')
else:
    print('Operação inválida')