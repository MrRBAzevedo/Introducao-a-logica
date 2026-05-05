soma = 0

for i in iter(int, 1):
    n = float(input())

    if n < 0:
        break
    else:
        soma += n

print(soma)