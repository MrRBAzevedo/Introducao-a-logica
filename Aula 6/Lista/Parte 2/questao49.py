limite = int(input())
contador = 1
valores = []

while contador <= limite:
    valor = int(input())
    valores.append(valor)

    contador += 1

soma = sum(valores)
media = soma / len(valores)
maior = max(valores)
menor = min(valores)
acima = 0

contador = 0
while contador < limite:
    if valores[contador] > media:
        acima += 1
    contador += 1

print(f'A soma dos valores é: {soma}')
print(f'A média dos valores é: {media}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
print(f'O número de valores acima da média é: {acima}')