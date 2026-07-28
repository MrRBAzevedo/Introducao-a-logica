n = int(input())
circ = list(map(int, input().split()))
metade = sum(circ) / 2
pares = 0

if metade % 1 != 0:
    print('N')
else:
    soma = 0

    for i in range(n):
        soma += circ[i]
        if soma >= metade:
            tamanho = i + 1
            break

    for i in range(tamanho):
        ponteiro = i
        distacia = 0

        while distacia < metade:
            distacia += circ[ponteiro]
            ponteiro = (ponteiro + 1) % n

        if distacia == metade:
            pares += 1

            if pares > 1:
                print('S')
                break
    else:
        print('N')
