n, s = map(int, input().split())
lista = list(map(int, input().split()))

for item in lista:
    if s - item in lista:
        print('SIM')
        break
else:
    print('NÂO')

