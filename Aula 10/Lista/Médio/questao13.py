n = int(input())
lista = list(map(int, input().split()))
lista.sort()
menor_diferenca = lista[1] - lista[0]

for i in range(2, n):
    diferenca = lista[i] - lista[i - 1]
    if diferenca < menor_diferenca:
        menor_diferenca = diferenca

print(menor_diferenca)