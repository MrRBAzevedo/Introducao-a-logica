n = int(input())
pos = 0
neg = 0

for i in range(n):
    num = float(input())

    if num > 0:
        pos += num
    else:
        neg += num

print(f'Soma dos positivos: {pos}')
print(f'Soma dos negativos: {neg}')