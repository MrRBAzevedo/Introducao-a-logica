def numero_vogais(palavra):
    palavra = list(palavra)
    resultado = 0

    for letra in palavra:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            resultado += 1

    return resultado

def main():
    palavra = input().lower()
    print(numero_vogais(palavra))

if __name__ == '__main__':
    main()
