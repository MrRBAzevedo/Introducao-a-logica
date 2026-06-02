def inverter(nome):
    saida = ''

    for i in range(len(nome)):
        posicao = len(nome) - i - 1
        saida += nome[posicao]

    return saida

def main():
    nome = input()
    print(inverter(nome))

if __name__ == '__main__':
    main()