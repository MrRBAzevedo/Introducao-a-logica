T = int(input())
N = int(input())
X = [int(input()) for _ in range(N)]
X.sort()
distancias = [X[0]]

for i in range(1, N):
    distancias.append(X[i] - X[i - 1])
distancias.append(T - X[N - 1])

menor_vizinhanca = distancias[0] + distancias[1] / 2

for i in range(1, N - 1):
    vizinhanca = (distancias[i] + distancias[i + 1]) / 2
    if vizinhanca < menor_vizinhanca:
        menor_vizinhanca = vizinhanca

vizinhanca = distancias[N - 1] / 2 + distancias[N]
if vizinhanca < menor_vizinhanca:
    menor_vizinhanca = vizinhanca

print(f'{menor_vizinhanca:.2f}')