dividendo = float(input('Insira o dividendo: '))
divisor = float(input('Insira o divisor: '))

if divisor == 0:
    print('Não há divisão por 0')
else:
    print(f'A divisão de {dividendo} por {divisor} resulta em {dividendo / divisor}')