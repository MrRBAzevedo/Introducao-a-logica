num = int(input())
divisores = []
divisor = 1

while divisor <= num:
    if num % divisor == 0:
        divisores.append(divisor)
    
    divisor += 1

print(f'D({num}) = {divisores}')