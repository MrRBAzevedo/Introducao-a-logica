pos = 0
neg = 0
zero = 0

for i in range(10):
    num = int(input())

    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print(f'{pos} números positivos')
print(f'{neg} números negativos')
print(f'{zero} números zeros')