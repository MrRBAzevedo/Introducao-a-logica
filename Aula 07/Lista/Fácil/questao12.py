num = list(input())
contador = len(num) - 1
inv = []

while contador >= 0:
    inv.append(num[contador])
    contador -= 1

contador = 0
while contador < len(inv):
    print(inv[contador], end = '')
    contador += 1
