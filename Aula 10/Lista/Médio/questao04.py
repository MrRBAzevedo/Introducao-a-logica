n = int(input())
lista = list(map(int, input().split()))
sequencia = 1
maior_sequencia = 1

for i in range(1, n):
    if lista[i] >= lista[i - 1]:
        sequencia += 1
        if sequencia > maior_sequencia:
            maior_sequencia = sequencia
    else:
        sequencia = 1

print(maior_sequencia)