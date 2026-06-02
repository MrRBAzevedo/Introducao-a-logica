def primo(numero):
    if numero > 1:
        div = 2

        while div < numero:
            if numero % div == 0:
                return False

            div += 1
        else:
            return True
    else:
        raise ValueError('Insira um número maior que 1')
        
def main():
    numero = int(input())
    print(primo(numero))

if __name__ == '__main__':
    main()

