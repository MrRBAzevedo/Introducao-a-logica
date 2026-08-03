S, T, P = map(int, input().split())
A = list(map(int, input().split()))
Mapa = [[] for _ in range(S)]

for i in range(T):
    n1, n2 = map(int, input().split())

    if A[n1 - 1] > A[n2 - 1]:
        Mapa[n1 - 1].append(n2 - 1)
    elif A[n2 - 1] > A[n1 - 1]:
        Mapa[n2 - 1].append(n1 - 1)

cam = [-1] * S

def busca(grafo, no_inicial):
    if cam[no_inicial] != -1:
        return cam[no_inicial]
    
    maior = 0
    
    for vizinho in grafo[no_inicial]:
        maior = max(maior, 1 + busca(grafo, vizinho))
    
    cam[no_inicial] = maior
    return maior 

print(busca(Mapa, P-1))
