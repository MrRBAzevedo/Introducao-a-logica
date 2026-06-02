a1 = int(input())
r = int(input())
S_max = int(input())
contador = 1
soma = 0

while soma <= S_max and contador <= 1000:
    num = a1 + (contador - 1) * r
    soma += num
    contador += 1

print(contador)