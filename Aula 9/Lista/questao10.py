def soma_alg(numero):
    numero = list(str(numero))
    numero = [int(digito) for digito in numero]
    
    return sum(numero)

def main():
    numero = int(input())
    print(soma_alg(numero))

if __name__ == '__main__':
    main()