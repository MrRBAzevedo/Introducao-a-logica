peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
imc = peso / altura ** 2

print('Peso normal' if imc < 25 else 'Acima do peso')