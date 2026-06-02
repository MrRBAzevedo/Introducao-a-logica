num = input()
lista = list(num)
lista = [int(dig) for dig in num]
soma = 0

for dig in lista:
    soma += dig ** len(lista)

if soma == int(num):
    print('Armstrong')
else:
    print('Não Armstrong')