num = int(input('Insira um número: '))
cont = 0

while num >= 10:
    num /= 10
    cont += 1

print(f'{num * 10**cont:.0f} = {num:.{cont}f} x 10^{cont}')

