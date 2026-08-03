import sys

sys.setrecursionlimit(10**6)

# Leitura da entrada
S, T, P = map(int, input().split())
altura = [0] + list(map(int, input().split()))

# Lista de adjacência
adj = [[] for _ in range(S + 1)]

for _ in range(T):
    u, v = map(int, input().split())

    if altura[u] > altura[v]:
        adj[u].append(v)
    elif altura[v] > altura[u]:
        adj[v].append(u)

# Memoização
dp = [-1] * (S + 1)

def dfs(u):
    if dp[u] != -1:
        return dp[u]

    dp[u] = 0

    for v in adj[u]:
        dp[u] = max(dp[u], 1 + dfs(v))

    return dp[u]

print(dfs(P))