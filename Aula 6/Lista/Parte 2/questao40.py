num = int(input())
divisor = 1
divisores = []

while divisor < num:
    if num % divisor == 0:
        divisores.append(divisor)
    
    divisor += 1

if sum(divisores) == num:
    print(f'{num} é um número perfeito')
else:
    print(f'{num} não é um número perfeito')