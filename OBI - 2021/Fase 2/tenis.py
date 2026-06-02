a = int(input())
b = int(input())
c = int(input())
d = int(input())

maior = max(a, b, c, d)
menor = min(a, b, c, d)
equipe_a = menor + maior
equipe_b = a + b + c + d - equipe_a

print(abs(equipe_a - equipe_b))