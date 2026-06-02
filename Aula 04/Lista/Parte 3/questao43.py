idade = int(input('Insira a idade: '))

if idade <= 5:
    print('Ingresso gratuito')
elif idade <= 12:
    print('Ingresso: R$ 12.00')
elif idade <= 17:
    print('Ingresso: R$ 18.00')
else:
    print('Ingresso: R$ 25.00')