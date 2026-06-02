def binario(num, tamanho):
    binario = ''

    while num != 0:
        dig = num % 2
        binario += str(dig)

        num = num // 2

    while len(binario) < tamanho:
        binario += '0'

    binario = binario[::-1]

    return binario

def soma(num1, num2):
    resultado = ''
    contador = 0
    
    while contador < len(num1):
        if num1[contador] != num2[contador]:
            resultado += '1'
        else:
            resultado += '0'

        contador += 1
    
    return resultado

K = int(input())
pilhas = []
pilhas_bin = []

for i in range(K):
    pilha = int(input())
    pilhas.append(pilha)

tamanho = len(bin(max(pilhas))[2:])

for pilha in pilhas:
    bin = binario(pilha, tamanho)
    pilhas_bin.append(bin)

resultado = binario(0, tamanho)

for pilha in pilhas_bin:
    resultado = soma(pilha, resultado)

if int(resultado) == 0:
    print('Perde')
else:
    print('Ganha')

