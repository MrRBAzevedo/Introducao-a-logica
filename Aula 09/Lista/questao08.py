def conv(celsius):
    return celsius * 9/5 + 32

def main():
    celsius = float(input('Insira a temperatura em celsius: '))

    print(f'A temperatura equivalente em fahrenheit é: {conv(celsius)}')

if __name__ == '__main__':
    main()