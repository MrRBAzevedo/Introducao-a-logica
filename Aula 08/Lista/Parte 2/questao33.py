soma_p = 0
soma_i = 0

for i in iter(int, 1):
    num = int(input())

    if num == 0:
        break
    elif num % 2 == 0:
        soma_p += num
    else:
        soma_i += num

print(f'Soma dos números pares: {soma_p}')
print(f'Soma dos números ímpares: {soma_i}')