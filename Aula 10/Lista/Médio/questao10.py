n, soma = map(int, input().split())
lista = list(map(int, input().split()))
inicio = 0
fim = 1
soma_atual = lista[0]

while fim < n:
    if soma_atual == soma:
        print('SIM')
        break
    elif soma_atual < soma:
        soma_atual += lista[fim]
        fim += 1
    else:
        soma_atual -= lista[inicio]
        inicio += 1
else:
    print('NÃO')