n, soma = map(int, input().split())
lista = list(map(int, input().split()))
lista.sort()
encontrado = False

for i in range(n - 2):
    if i > 0 and lista[i] == lista[i - 1]:
        continue

    pon_esq = i + 1
    pon_dir = n - 1

    while pon_esq < pon_dir:
        soma_atual = lista[i] + lista[pon_esq] + lista[pon_dir]

        if soma_atual == soma:
            if lista[i] != lista[pon_esq] and lista[i] != lista[pon_dir] and lista[pon_dir] != lista[pon_esq]:
                print('Encontrado')
                encontrado = True
                break
            else:
                pon_esq += 1
                pon_dir -= 1
        elif soma_atual < soma:
            pon_esq += 1
        else:
            pon_dir -= 1

    if encontrado:
        break

if not encontrado:
    print('Não encontrado')