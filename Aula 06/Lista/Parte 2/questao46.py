numeros = []
n = int(input())

for i in range(n):
    num = float(input())

    if num < 10:
        cod = {'numero' : num, 'class' : 'pequeno'}
    elif num <= 100:
        cod = {'numero' : num, 'class' : 'médio'}
    else:
        cod = {'numero' : num, 'class' : 'grande'}

    numeros.append(cod)

for cod in numeros:
    print(f'O número {cod['numero']} é {cod['class']}')