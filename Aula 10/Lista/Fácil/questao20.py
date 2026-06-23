n = int(input())
lista = list(map(int, input().split()))
inversa = []

for i in range(n - 1, -1, -1):
    inversa.append(lista[i])

if lista == inversa:
    print('SIM')
else:
    print('NÃO')