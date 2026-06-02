import random
import subprocess

num = random.randint(1, 100)
chute = 0

while chute != num:
    subprocess.run('cls', shell = 'True')
    chute = int(input('Digite seu chute: '))

    if chute > num:
        print('Muito alto!')
        input()
    elif chute < num:
        print('Muito baixo!')
        input()
    else:
        print('Você acertou!')
