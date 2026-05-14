def par(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

def main():
    num = int(input())

    print(f'O número {num} é {par(num)}')

if __name__ == '__main__':
    main()