n = int(input())
lista_a = list(map(int, input().split()))
m = int(input())
lista_b = list(map(int, input().split()))
contador_a = 0
contador_b = 0
nova_lista = []

while contador_a < n and contador_b < m:
    nova_lista.append(lista_b[contador_b])
    contador_b += 1
    nova_lista.append(lista_a[contador_a])
    contador_a += 1

if contador_a != n:
    nova_lista.extend(lista_a[contador_a:])
if contador_b != m:
    nova_lista.extend(lista_b[contador_b:])

print(*nova_lista)
