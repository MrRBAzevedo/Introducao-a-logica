n, k = map(int, input().split())
lista = list(map(int, input().split()))
k %= n
dicionario = {}

for i, valor in enumerate(lista):
    dicionario[(i + k) % n] = valor

for i in range(n):
    print(dicionario[i], end = ' ')

print()