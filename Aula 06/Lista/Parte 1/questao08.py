from itertools import product


contador = 1
produto = 1
limite = int(input())

while contador <= limite:
    produto *= contador
    # produto = produto * contador
    contador += 1
    
print(produto)