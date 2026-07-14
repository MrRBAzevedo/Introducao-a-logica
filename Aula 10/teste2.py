lista1 = [1, 4, 7, 10, 11]
lista2 = [2, 3, 6, 8, 9]
lista_nova = [1, 2, 3, 6, 7, 8, 9]
print(lista_nova)

ponteiro1 = 3
print(lista1[ponteiro1:len(lista1)])
lista_nova += lista1[ponteiro1:len(lista1)]
print(lista_nova)