def media(numeros):
    return sum(numeros) / len(numeros)

def main():
    numeros = []
    for i in range(4):
        numero = float(input())
        numeros.append(numero)

    print(media(numeros))

if __name__ == '__main__':
    main()