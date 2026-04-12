nota = int(input('Insira a nota: '))
if nota < 0 or nota > 100:
    raise ValueError('A nota deve ser um número entre 0 e 100')

if nota >= 90:
    print('Excelente')
elif nota >= 70:
    print('Bom')
elif nota >= 50:
    print('Regular')
else:
    print('Insuficiente')