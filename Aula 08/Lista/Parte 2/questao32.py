n = int(input())
divisores = []

for div in range(1, n + 1):
    if n % div == 0:
        divisores.append(div)

print(f'D({n}): {divisores}')