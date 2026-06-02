seq = []
entrada = 0

while entrada != -1:
    entrada = int(input())
    seq.append(entrada)

tartaruga = seq[0]
lebre = seq[seq[0]]

while tartaruga != -1:
    if lebre == tartaruga:
        lebre = seq[tartaruga]
        tamanho = 1
        while lebre != tartaruga:
            lebre = seq[lebre]
            tamanho += 1

        print('Há ciclo')
        print(f'Tamanho do ciclo: {tamanho}')

        break

    tartaruga = seq[tartaruga]
    lebre = seq[seq[lebre]]
else:
    print('Não há ciclo')