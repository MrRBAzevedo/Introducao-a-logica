velocidade = float(input('Insira a velocidade: '))

if velocidade <= 80:
    print('Sem multa')
elif velocidade <= 100:
    print('Multa leve: R$ 130.00')
elif velocidade <= 120:
    print('Multa leve: R$ 195.00')
else:
    print('Multa grave: R$ 293 + suspensão')