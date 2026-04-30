num = input()
lista = list(num)
rev = list(reversed(num))

if lista == rev:
    print(f'O número {num} é um palíndromo')
else:
    print(f'O número {num} não é um palíndromo')