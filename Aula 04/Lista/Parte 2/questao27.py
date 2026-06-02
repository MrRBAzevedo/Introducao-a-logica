ano_nascimento = int(input('Insira seu ano de nascimento: '))

print('Elegível à aposentadoria' if 2026 - ano_nascimento >= 65 else 'Não elegível ainda')