def extremos(valores):
    valores = [int(valor) for valor in valores]
    maior = valores[0]
    menor = valores[1]

    for valor in valores:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    return f'{menor} {maior}' 

def main():
    n = int(input())
    valores = input().split()

    print(extremos(valores))

if __name__ == '__main__':
    main()