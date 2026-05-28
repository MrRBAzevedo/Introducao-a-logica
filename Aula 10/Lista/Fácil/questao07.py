def rotacao(lista):
    lista.insert(0, lista[-1])
    lista.pop(-1)

    return lista

def main():
    n = int(input())
    lista = input().split()

    if len(lista) != n: 
        raise ValueError('A quantidade de valores digitados é diferente da indicada')
    else:
        rotacao(lista)       
        for item in lista:
            print(item, end = ' ')


if __name__ == '__main__':
    main()