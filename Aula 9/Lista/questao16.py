def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False

def main():
    ano = int(input())
    print(bissexto(ano))

if __name__ == '__main__':
    main()