n = int(input())
lista = list(map(int, input().split()))
contador = 1
tamanho = n

for i in range(n - 1):
    lista_e = lista[:contador]
    lista_d = lista[contador + 1:]
    lista = lista_e + lista_d

    tamanho -= 1
    contador = (contador + 1) % tamanho

print(lista[0])








# contador = 1

# lista = [1, 2, 3, 4, 5]
# lista1 = lista[:contador]
# lista2 = lista[contador + 1:]
# lista = lista1 + lista2
# # 
# # contador = (contador + 1) % n 

# print(lista)