n = int(input())
lista = list(map(int, input().split()))
lista.sort()
menores = lista[0] * lista[1]
maiores = lista[-1] * lista[-2]


if maiores > menores: print(maiores)
else: print(menores)