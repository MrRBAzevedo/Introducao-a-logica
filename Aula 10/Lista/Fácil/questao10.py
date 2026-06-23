n = int(input())
valores = list(map(int, input().split()))
x = int(input())
indice = -1

for i in range(n):
    if valores[i] == x:
        indice = i

print(indice)