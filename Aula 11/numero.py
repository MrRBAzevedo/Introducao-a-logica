import random

numero = random.randint(1, 100)
chute = int(input('Digite um número entre 1 e 100: '))

while chute != numero:
    if chute > numero:
        print(f'O número é menor que {chute}')
    else:
        print(f'O número é maior que {chute}')

    chute = int(input('Digite um novo número: '))

print(f'Parabéns! Você acertou o número {numero}')