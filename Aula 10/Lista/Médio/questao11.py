n, soma = map(int, input().split())
lista = list(map(int, input().split()))
sublistas = 0
menor = 0
maior = 1
soma_atual = lista[0]

while maior <= n:
    if soma_atual == soma:
        sublistas += 1
        if maior < n: soma_atual += lista[maior]
        maior += 1
    elif soma_atual < soma:
        if maior < n: soma_atual += lista[maior]
        maior += 1
    else:
        soma_atual -= lista[menor]
        menor += 1

    print(soma_atual)
    print(lista[menor:maior])

print(sublistas)