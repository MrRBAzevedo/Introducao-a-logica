def encontrar(lista, valor):
    for item in lista:
        if valor == item:
            return lista.index(valor)
    else:
        return -1

lista = input().split()
lista = []
valor = int(input())