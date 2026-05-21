def fatorial(numero):
    resultado = 1
    if numero >= 0:
        while numero > 0:
            resultado *= numero
            numero -= 1
           
        return(resultado)
    else:
        raise ValueError('Insira um valor positivo')

def main():
    numero = int(input())
    print(fatorial(numero))

if __name__ == '__main__':
    main()