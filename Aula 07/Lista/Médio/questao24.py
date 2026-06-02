N = int(input())
K = 1

while K ** 2 < N:
    K += 1

print(K - 1)