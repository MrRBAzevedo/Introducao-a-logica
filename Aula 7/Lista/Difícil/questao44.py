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
        print(arvore)
        print(profundidade)
        break