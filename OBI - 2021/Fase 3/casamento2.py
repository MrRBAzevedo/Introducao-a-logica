from collections import deque

a = [int(num) for num in input()]
b = [int(num) for num in input()]
a = deque(a)
b = deque(b)
tamanho_a = len(a)
tamanho_b = len(b)

if tamanho_a > tamanho_b:
    diferenca = tamanho_a - tamanho_b

    for i in range(diferenca):
        b.appendleft(0)
elif tamanho_a < tamanho_b:
    diferenca = tamanho_b - tamanho_a

    for i in range(diferenca):
        a.appendleft(0)

num_a = []
num_b = []

for i in range(max(tamanho_b, tamanho_a)):
    dig_a = a[i]
    dig_b = b[i]

    if dig_a > dig_b:
        num_a.append(dig_a)
    elif dig_b > dig_a:
        num_b.append(dig_b)
    else:
        num_a.append(dig_a)
        num_b.append(dig_b)

if num_a:
    resultado_a = ''
    for i in range(len(num_a)):
        resultado_a += str(num_a[i])

    resultado_a = int(resultado_a)
else:
    resultado_a = -1

if num_b:
    resultado_b = ''
    for i in range(len(num_b)):
        resultado_b += str(num_b[i])

    resultado_b = int(resultado_b)
else:
    resultado_b = -1

print(f'{resultado_a} {resultado_b}' if resultado_b > resultado_a else f'{resultado_b} {resultado_a}')