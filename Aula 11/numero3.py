import random

soma = 0
n = int(input())

for i in range(n):
    tentativas = 1
    chute = 0
    limite_inferior = 1
    limite_superior = 1000000
    numero = random.randint(limite_inferior, limite_superior) 

    while True:
        chute = (limite_superior - limite_inferior) // 2 + limite_inferior
        print(f'Digite um número entre {limite_inferior} e {limite_superior}: {chute}')

        if chute == numero: break
        elif chute > numero: limite_superior = min(chute, limite_superior)
        else: limite_inferior = max(chute, limite_inferior)

        tentativas += 1

    soma += tentativas

print()
print(soma / n)