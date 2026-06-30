n, k = map(int, input().split())
lista_original = list(map(int, input().split()))
lista = []

for i in range(n):
    if lista.count(lista_original[i]) < k:
        lista.append(lista_original[i])

# for item in lista:
#     print(item, end = ' ')

print(*lista)