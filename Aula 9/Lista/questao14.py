def palindromo(palavra):
    palavra = list(palavra)

    if palavra == palavra[::-1]:
        return True
    else:
        return False

def main():
    palavra = input()
    print(palindromo(palavra))

if __name__ == '__main__':
    main()