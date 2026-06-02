import subprocess

def exibir_menu():
    subprocess.run('cls', shell = True)
    print('Lanches da lanchonete\n')
    print('1 - Hambúrguer: R$ 18.00')
    print('2 - Hot-dog: R$ 12.00')
    print('3 - Suco: R$ 8.00')
    print('4 - Refrigerante: R$ 6.00')
    print('5 - Sair sem pedir\n')

def escolher_opcao():
    escolha = input('Escolha uma opção: ')
    
    if escolha == '1':
        exibir_preco(18)
    elif escolha == '2':
        exibir_preco(12)
    elif escolha == '3':
        exibir_preco(8)
    elif escolha == '4':
        exibir_preco(6)
    elif escolha == '5':
        print('\nSeja sempre bem-vindo')
    else:
        print('\nOpção inválida')
    
def exibir_preco(escolha):
    quantidade = int(input('Insira a quantidade desejada: '))
    print(f'\nO total a pagar é: R$ {escolha * quantidade:.2f}')

def main():
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()