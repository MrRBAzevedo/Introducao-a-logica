notas = map(float, input().split())
media = sum(notas) / 3

print('Em recuperação' if 5 <= media < 7 else 'Fora de recuperação')