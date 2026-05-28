n = int(input())
lista = input().split()
lista = [int(item) for item in lista]
x = int(input())

if len(lista) != n: 
    raise ValueError('A quantidade de valores digitados é diferente da indicada')
else:
    if x in lista: print('SIM')
    else: print('NÃO')