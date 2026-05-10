chave = 'termo'
chave = list(chave)

while True:
    entrada = list(input().lower())

    if len(entrada) != 5:
        print('Insira somente palavras com 5 letras')
        continue

    if entrada == chave:
        print('Você descobriu a palavra chave!')
        break
    else:
        dica = ''

        for i in range(5):
            if entrada[i] == chave[i]:
                dica += 'C'
            elif entrada[i] in chave:
                dica += 'L'
            else:
                dica += 'E'

        print(dica)
    
