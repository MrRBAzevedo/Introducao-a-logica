n = int(input())
lista1 = list(map(int, input().split()))
m = int(input())
lista2 = list(map(int, input().split()))
lista_nova = []
ponteiro1 = 0
ponteiro2 = 0

while ponteiro1 < n and ponteiro2 < m:
    if lista1[ponteiro1] < lista2[ponteiro2]:
        lista_nova.append(lista1[ponteiro1])
        ponteiro1 += 1
    else:
        lista_nova.append(lista2[ponteiro2])
        ponteiro2 += 1

if ponteiro1 < n:
    lista_nova += lista1[ponteiro1:n]
if ponteiro2 < m:
    lista_nova += lista2[ponteiro2:m]

print(*lista_nova)
