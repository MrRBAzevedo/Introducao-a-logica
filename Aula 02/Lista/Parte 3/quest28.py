print('Calculador de notas do IFRN\n')

n1, n2, n3, n4 = map(int, input('Insira suas notas: ').split())

print(f'\nPrimeiro bimestre: {n1}')
print(f'Segundo bimestre: {n2}')
print(f'Terceiro bimestre: {n3}')
print(f'Quarto bimestre: {n4}\n')

media = (n1 * 2 + n2 * 2 + n2 * 3 + n4 * 3) / 10
print(f'Sua média final é: {media}')
print(f'Você está {'aprovado' if (media >= 60) else 'em recuperação'}.')
