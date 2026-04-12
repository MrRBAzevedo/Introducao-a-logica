conta = float(input('Insira o consumo em kWh: '))

if conta <= 100:
    print(f'O total a pagar é: R$ {conta * 0.4:.2f}')
elif conta <= 200:
    print(f'O total a pagar é: R$ {conta * 0.5:.2f}')
elif conta <= 300:
    print(f'O total a pagar é: R$ {conta * 0.65:.2f}')
else:
    print(f'O total a pagar é: R$ {conta * 0.85:.2f}')