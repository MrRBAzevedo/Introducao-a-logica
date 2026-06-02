n = int(input())
lista = input().split()
lista = [int(num) for num in lista]
contracoes = 0

esquerda = 0
direita = len(lista) - 1

while esquerda < direita:
    if lista[esquerda] == lista[direita]:
        esquerda += 1
        direita -= 1
    elif lista[esquerda] < lista[direita]:
        lista[esquerda + 1] += lista[esquerda]
        contracoes += 1
        esquerda += 1
    else:
        lista[direita - 1] += lista[direita]
        contracoes += 1
        direita -= 1

print(contracoes)