def acima(valores):
    valores = [int(valor) for valor in valores]
    media = sum(valores) / len(valores)
    resultado = 0

    for valor in valores:
        if valor > media: resultado += 1

    return resultado

def main():
    n = int(input())
    valores = input().split()

    if len(valores) != n: 
        raise ValueError('A quantidade de valores digitados é diferente da indicada')
    else:
        print(acima(valores))

if __name__ == '__main__':
    main()


