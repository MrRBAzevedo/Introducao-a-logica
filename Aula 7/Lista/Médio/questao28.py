import math

num = list(input())
contador = 0

while len(num) != 1:
    num = [int(dig) for dig in num]
    num = math.prod(num)
    num = list(str(num))

    contador += 1

print(f'Persistência: {contador}')