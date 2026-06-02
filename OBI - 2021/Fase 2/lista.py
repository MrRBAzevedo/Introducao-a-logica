def palindromo(lista):
    if lista == lista[::-1]:
        return True
    else:
        return False

def cortar(lista):
    while True:
        if lista[0] == lista[-1]:
            lista.pop(0)
            lista.pop(-1)
        else:
            break
    
    return lista

def contracao(lista):
    lista1 = lista[0:len(lista)]
    lista2 = lista[0:len(lista)]

    lista1[0] = lista1[0] + lista[1]
    lista1.pop(1)
    lista2[-1] = lista2[-1] + lista2[-2]
    lista2.pop(-2)
    
    return lista1, lista2

n = int(input())
lista = []
listas = []
contracoes = 0

lista = input().split()
lista = [int(num) for num in lista]

listas.append(lista)

while True:
    found = False
    novas_listas = []

    for lista in listas:
        if palindromo(lista):
            found = True

    if found == True:
        print(contracoes)
        break

    for lista in listas:
        lista = cortar(lista)

    for lista in listas:
        nova_lista1, nova_lista2 = contracao(lista)
        novas_listas.append(nova_lista1)
        novas_listas.append(nova_lista2)

    listas = novas_listas.copy()
    novas_listas = []
    contracoes += 1