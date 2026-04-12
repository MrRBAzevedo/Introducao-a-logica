mes = int(input('Insira o mês em número: '))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    print('Esse mês possui 31 dias')
elif mes in [4, 6, 9, 11]:
    print('Esse mês possui 30 dias')
elif mes == 2:
    print('Esse mês possui 28 dias')
else:
    print('Valor inválido')
