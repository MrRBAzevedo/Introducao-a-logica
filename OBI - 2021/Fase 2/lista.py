n = int(input())
lista = []

for i in range(n):
    valor = int(input())
    lista.append(valor)

while True:
    if lista[0] == lista[-1]:
        lista.remove(0)
        lista.pop()