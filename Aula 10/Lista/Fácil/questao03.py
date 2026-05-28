def pares(valores):
    valores = [int(valor) for valor in valores]
    soma = 0

    for valor in valores:
        if valor % 2 == 0: soma += 1

    return soma

def main():
    n = int(input())
    valores = input().split()

    print(pares(valores))

if __name__ == '__main__':
    main()
