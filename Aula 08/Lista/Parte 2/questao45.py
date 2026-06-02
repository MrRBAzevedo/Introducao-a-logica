inicio = int(input())
fim = int(input())
primos = []

for num in range(inicio, fim + 1):
    div = 2
    while div < num:
        if num % div == 0:
            break
        
        div += 1
    else:
        primos.append(num)

print(sum(primos))
