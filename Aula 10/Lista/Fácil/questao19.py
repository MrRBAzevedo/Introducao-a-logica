n = int(input())
valores = list(map(int, input().split()))
diferenca = 0

for i in range(n - 1):
    dif = abs(valores[i] - valores[i + 1])
    if dif > diferenca:
        diferenca = dif

print(diferenca)