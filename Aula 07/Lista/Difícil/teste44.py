arvore = [[0, 1], [1, 4], [1, 3], [2, 5], [1, 2], [3, 5], [2, 3], [3, 4], [1, 1], [4, 3], [3, 2], [5, 3], [2, 1], [5, 2], [3, 1], [4, 1], [1, 0]]
fracao = [5, 3]

profundidade = 4
sequencia = ''

for i in range(1, profundidade):
    metade = len(arvore) / 2
    index = arvore.index(fracao)
    if index < metade:
        arvore = arvore[0:int(metade + 0.5)]
        sequencia += 'L'
    elif index > metade:
        arvore = arvore[int(metade - 0.5):len(arvore)]
        sequencia += 'R'
    print(arvore)
    
print(sequencia)
