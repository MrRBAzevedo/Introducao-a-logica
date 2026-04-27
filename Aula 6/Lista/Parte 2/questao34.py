n1 = int(input())
n2 = int(input())
dividendo = max(n1, n2)
divisor = min(n1, n2)

while True:
    if dividendo % divisor == 0:
        break
    
    novo_dividendo = divisor
    divisor = dividendo % divisor
    dividendo = novo_dividendo

    

print(f'O MDC de {n1} e {n2} é {divisor}')
