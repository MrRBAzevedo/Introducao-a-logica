n = int(input())
contador = 1
num_ant = int(input())
tamanho = 1

while contador < n:
    num = int(input())

    if num == num_ant + 1:
        tamanho += 1
    else:
        tamanho = 1

    num_ant = num
    contador += 1

print(tamanho)

