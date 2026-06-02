mes = int(input('Insira o mês em número: '))

if mes in [12, 1, 2]:
    print('Verão')
elif mes in [3, 4, 5]:
    print('Outono')
elif mes in [6, 7, 8]:
    print('Inverno')
elif mes in [9, 10, 11]:
    print('Primavera')
else:
    print('O valor inserido é inválido')