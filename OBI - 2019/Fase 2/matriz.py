L, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(L)]

alturas = [0] * (C - 1)

resposta = 0

for i in range(L - 1):

    for j in range(C - 1):
        if A[i][j] + A[i + 1][j + 1] <= A[i][j + 1] + A[i + 1][j]:
            alturas[j] += 1
        else:
            alturas[j] = 0

    pilha = []

    for j in range(C):

        atual = 0 if j == C - 1 else alturas[j]

        while pilha and alturas[pilha[-1]] >= atual:

            h = alturas[pilha.pop()]

            if pilha:
                w = j - pilha[-1] - 1
            else:
                w = j

            resposta = max(resposta, (h + 1) * (w + 1))

        if j < C - 1:
            pilha.append(j)

print(resposta)