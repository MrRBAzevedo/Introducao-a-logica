rep = int(input())
pilhas = []

for i in range(rep):
    a, b = map(int, input().split())
    pil = min(a, b)
    div = 2

    while pil != div:
        if a % pil == 0 and b % pil == 0:
            pilhas.append(pil)
            break

        pil = int(min(a, b) / div)
        div += 1

for pil in pilhas:
    print(pil)