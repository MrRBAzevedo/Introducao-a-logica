pessoas = []
num = 1

for i in range(2):
    pessoas.append(input('Insira o nome da pessoa: '))

for pessoa in pessoas:
    print(f'Pessoa {num}: {pessoa}')
    num += 1
    