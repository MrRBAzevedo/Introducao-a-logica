tamanho = 8

num = int(input())
binario = ''

while num != 0:
    dig = num % 2
    binario += str(dig)

    num = num // 2

while len(binario) < tamanho:
    binario += '0'

binario = binario[::-1]

print(binario)