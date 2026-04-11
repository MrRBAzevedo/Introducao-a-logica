salario = float(input('Insira o salário atual: '))

if salario <= 1500:
    reajuste = salario * 0.15
    print(f'O reajuste será de R$ {reajuste:.2f}')
    print(f'O novo salário será de R$ {(salario + reajuste):.2f}')
elif salario <= 3000:
    reajuste = salario * 0.1
    print(f'O reajuste será de R$ {reajuste:.2f}')
    print(f'O novo salário será de R$ {(salario + reajuste):.2f}')
elif salario <= 6000:
    reajuste = salario * 0.07
    print(f'O reajuste será de R$ {reajuste:.2f}')
    print(f'O novo salário será de R$ {(salario + reajuste):.2f}')
else:
    reajuste = salario * 0.03
    print(f'O reajuste será de R$ {reajuste:.2f}')
    print(f'O novo salário será de R$ {(salario + reajuste):.2f}')