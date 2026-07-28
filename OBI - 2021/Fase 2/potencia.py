n = int(input())
entrada = [int(input()) for num in range(n)]
valores = []

for valor in entrada:
    base = valor // 10
    expoente = valor % 10

    valores.append(base ** expoente)

print(sum(valores))