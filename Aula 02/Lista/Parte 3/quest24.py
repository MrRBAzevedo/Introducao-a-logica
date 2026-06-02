nome = input('Insira seu nome: ')
idade = int(input('Insira sua idade: '))

plural = 'ano' if (idade == 1) else 'anos'

print(f'{nome} tem {idade} {plural}.')