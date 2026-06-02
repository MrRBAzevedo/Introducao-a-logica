n = int(input())
pares = []

for i in range(n):
    a, b = map(int, input().split())
    pares.append((a, b))

for par in pares:
    if par[0] > par[1]:
        print(f'{par[0]} é o maior e {par[1]} é o menor')
    elif par[0] < par[1]:
        print(f'{par[1]} é o maior e {par[0]} é o menor')
    else:
        print(f'{par[0]} e {par[1]} são iguais')