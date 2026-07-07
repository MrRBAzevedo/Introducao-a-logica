n, soma = map(int, input().split())
lista = list(map(int, input().split()))
lista.sort()
pares = {}

for i, valor in enumerate(lista):
    complemento = soma - valor

    for j, num in enumerate(lista):
        if i != j:
            terceiro = complemento - num
            pares[terceiro] = (i, j)

    if valor in pares:
        if i not in pares[valor]:
            print('SIM')
            break
else:
    print('NÃO')


