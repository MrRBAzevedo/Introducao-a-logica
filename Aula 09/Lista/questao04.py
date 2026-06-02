def extremos(numeros):
    menor = numeros[0]
    maior = numeros[0]

    for numero in numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

    return (menor, maior)

def main():
    numeros = []

    for i in range(5):
        numero = int(input())
        numeros.append(numero)

    menor, maior = extremos(numeros)

    print(f'O maior dos números é {maior}')
    print(f'O menor dos números é {menor}')

if __name__ == '__main__':
    main()