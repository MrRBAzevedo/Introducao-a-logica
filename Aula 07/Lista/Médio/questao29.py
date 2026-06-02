contador = 0
contador_p = 0
soma = 0

while soma <= 1000:
    num = int(input())

    if num > 0:
        soma += num
        contador_p += 1
    
    contador += 1

print(f'Total lidos: {contador}')
print(f'Positivos: {contador_p}')