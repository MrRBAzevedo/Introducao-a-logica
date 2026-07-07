n, resultado = map(int, input().split())
lista = list(map(int, input().split()))
lista.sort()
pon_esq = 0
pon_dir = n - 1

while pon_esq < pon_dir:
    soma = lista[pon_esq] + lista[pon_dir]

    if soma == resultado:
        print('SIM')
        break
    elif soma < resultado:
        pon_esq += 1
    else:
        pon_dir -= 1
else:
    print('NÃO')