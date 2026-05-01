contador = int(input())

binario = bin(contador)[2:]
binario = list(str(binario))
binario = [int(bi) for bi in binario]
binario.insert(0, 0)
binario.insert(1, 0)
binario.insert(2, 0)
binario.append(0)

pares = 0
cont = 3

while cont < len(binario):
    if binario[cont] == 0 and binario[cont - 1] == 1 and binario[cont - 2] == 1 and binario[cont - 3] == 0:
        pares += 1
    
    cont += 1

print(pares)