import math

c1 = float(input('Insira a medida do primeiro cateto: '))
c2 = float(input('Insira a medida do segundo cateto: '))
hip = math.sqrt(c1 ** 2 + c2 ** 2)

print(f'A hipotenusa mede: {hip}')