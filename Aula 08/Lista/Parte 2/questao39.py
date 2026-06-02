import subprocess

def main():
    opcao = 1

    while opcao != 3:
        clear()
        print('''1 - Somar dois números
2 - Subtrair dois números
3 - Sair do sistema\n''')
        opcao = int(input())

        if opcao == 1:
            somar()
            input()
        elif opcao == 2:
            subtrair()
            input()
        elif opcao == 3:
            clear()
            print('Finalizando sistema...')
        else:
            print('Opcao inválida')
            input()

def somar():
    clear()
    print('Somando dois números\n')
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print(f'A soma de {x} e {y} é {x + y}')

def subtrair():
    clear()
    print('Subtraindo dois números')
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print(f'A diferença de {x} e {y} é {x - y}')

def clear():
    subprocess.run('cls', shell = True)

if __name__ == '__main__':
    main()
