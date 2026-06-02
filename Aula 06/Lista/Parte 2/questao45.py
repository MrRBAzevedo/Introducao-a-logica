inicio = int(input())
fim = int(input())
primos = []
divisor = 2

while inicio <= fim:
    while divisor < inicio:
        if inicio % divisor == 0:
            break
        
        divisor += 1
    else:
        primos.append(inicio)
    
    divisor = 2
    inicio += 1

print('Os primos entre esse intervalo são', end = ': ')
for number in primos:
    print(number, end = '; ')