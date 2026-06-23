n = int(input())
valores = list(map(int, input().split()))
x = int(input())
vezes = 0

for i in range(n):
    if valores[i] == x:
        vezes += 1

print(vezes)