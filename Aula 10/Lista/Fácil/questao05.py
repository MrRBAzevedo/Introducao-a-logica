def inverter(lista):
    resultado = []

    for index in range(1, len(lista) + 1):
        resultado.append(lista[len(lista) - index])

    return resultado


def main():
    n = int(input())
    lista = input().split()

    if len(lista) != n: 
        raise ValueError('A quantidade de valores digitados é diferente da indicada')
    else:
        lista = inverter(lista)
        for item in lista:
            print(item, end = ' ')

if __name__ == '__main__':
    main()
