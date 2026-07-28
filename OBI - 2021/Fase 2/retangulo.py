n = int(input())
l = list(map(int, input().split()))
metade = sum(l) / 2
pares = 0
ponteiro_i = 0
ponteiro_f = 1
soma = l[0]

while ponteiro_f < n:
    if soma < metade:
        soma += l[ponteiro_f]
        ponteiro_f += 1
    else:
        if soma == metade: pares += 1
        soma -= l[ponteiro_i]
        ponteiro_i += 1

    if pares == 2:
        print('S')
        break
else:
    print('N')