num = list(input())
num_inv = []
contador = len(num) - 1

while contador >= 0:
    num_inv.append(num[contador])
    contador -= 1

contador = 0
while contador < len(num_inv):
    print(num_inv[contador], end = '')
    contador += 1