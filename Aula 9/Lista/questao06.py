def soma(num):
    soma = 0

    while num > 0:
        soma += num
        num -= 1

    return soma

def main():
    numero = int(input())

    print(f'A soma dos número de 1 até {numero} é {soma(numero)}')

if __name__ == '__main__':
    main()