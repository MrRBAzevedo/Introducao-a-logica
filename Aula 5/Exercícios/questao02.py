dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))
if divisor == 0:
    print('Não existe divisão por zero')
else:
    quociente = dividendo / divisor
    print(f'Quociente: {quociente}')
