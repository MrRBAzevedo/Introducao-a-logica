n = int(input())
lista = list(map(int, input().split()))
lista_nova = [lista[0]]

for i in range(1, len(lista) - 1):
    if lista[i] <= lista[i - 1] or lista[i] <= lista[i + 1]:
        lista_nova.append(lista[i])

lista_nova.append(lista[-1])

for item in lista_nova:
    print(item, end = ' ')
