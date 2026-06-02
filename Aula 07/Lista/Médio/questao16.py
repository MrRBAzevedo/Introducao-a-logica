n = int(input())
step = 0
print(n)

while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        n += 1

    print(f'{n:.0f}')
    step += 1

print(step)