arvore = [[0, 1], [1, 0]]
p = int(input())
q = int(input())
fracao = [p, q]
profundidade = 0

while True:
    for duplicacao in range(0, 2 * (len(arvore) - 1), 2):
        filha = [arvore[duplicacao][0] + arvore[duplicacao + 1][0], arvore[duplicacao][1] + arvore[duplicacao + 1][1]]
        arvore.insert(duplicacao + 1, filha)

    profundidade += 1

    if fracao in arvore:      
        break

sequencia = ''


for i in range(1, profundidade):
    metade = len(arvore) / 2
    index = arvore.index(fracao)

    if index < metade:
        arvore = arvore[0:int(metade + 1/2)]
        sequencia += 'L'
    elif index > metade:
        arvore = arvore[int(metade - 1/2):len(arvore)]
        sequencia += 'R'
    
print(sequencia)
print(profundidade)