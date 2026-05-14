def ocorrencia(palavra, caractere):
    ocorrencias = 0

    for letra in palavra:
        if letra == caractere:
            ocorrencias += 1

    return ocorrencias

def main():
    palavra = input('Insira uma palavra: ')
    caractere = input('Insira um caractere: ')

    print(f'O caractere "{caractere}" apararece {ocorrencia(palavra, caractere)} vezes na palavra {palavra}')

if __name__ == '__main__':
    main()