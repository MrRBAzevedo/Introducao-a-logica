repeticoes = int(input('Digite a quantidade de números: '))
numeros = []

for i in range(repeticoes):
    num = int(input(f'Informe o valor {i + 1}: '))
    numeros.append(num)

media = sum(numeros) / len(numeros)
acima = 0
for numero in numeros:
    if numero > media: acima += 1

print(f'''a soma total é {sum(numeros)}
a média é {media}
o maior valor é {max(numeros)}
o menor valor é {min(numeros)}
a quatidade de valores acima da média é {acima}''')