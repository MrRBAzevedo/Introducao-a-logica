n = int(input())
div = 1
soma = 0

while div < n:
    if n % div == 0:
        soma += div

    div += 1

if soma == n:
    print('Perfeito')
else:
    print('Não perfeito')