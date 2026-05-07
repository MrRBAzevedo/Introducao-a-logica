import random
numero = random.randint(1, 100)

for i in iter(int, 1):
    chute = int(input())

    if chute == numero:
        print(f'Acertou! O número era {numero}.')
        break
    elif chute < numero:
        print(f'Muito baixo')
    else:
        print(f'Muito alto')
