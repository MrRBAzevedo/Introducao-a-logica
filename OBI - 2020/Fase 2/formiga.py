from collections import deque

S, T, P = map(int, input().split())
A = list(map(int, input().split()))
Mapa = [[] for _ in range(S)]

for i in range(T):
    n1, n2 = map(int, input().split())

    if A[n1 - 1] > A[n2 - 1]:
        Mapa[n1 - 1].append(n2 - 1)
    else:
        Mapa[n2 - 1].append(n1 - 1)

def busca(grafo, no_inicial):
    visitados = set()
    fila = deque([no_inicial])
    visitados.add(no_inicial)
    nivel = 0

    while fila:
        no_atual = fila.popleft()

        for vizinho in Mapa[no_atual]:            
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

