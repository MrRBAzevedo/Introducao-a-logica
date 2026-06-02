n = list(input())
it = 0

while len(n) != 1:
    n = [int(num) for num in n]
    n = sum(n)
    n = list(str(n))

    it += 1

print(f'Raiz: {n[0]}')
print(f'Iterações: {it}')