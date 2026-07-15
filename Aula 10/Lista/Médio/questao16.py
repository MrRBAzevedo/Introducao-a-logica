from collections import deque

n, k = map(int, input().split())
lista = list(map(int, input().split()))
lista = deque(lista)
k %= n

lista.rotate(k)

# for i in range(k):
#     lista.appendleft(lista[-1])
#     lista.pop()

print(*lista)