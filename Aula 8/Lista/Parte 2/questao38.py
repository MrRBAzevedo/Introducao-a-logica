n = int(input())
valores = []

for i in range(n):
    valor = int(input())
    valores.append(valor)

maior = valores[0]
menor = valores[0]

for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')