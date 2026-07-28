n, c, s = map(int, input().split())
x = list(map(int, input().split()))
if s == 1: passagens = 1
else: passagens = 0

posicao_atual = 1

for i in range(c):
    posicao_atual += x[i]

    if posicao_atual == s: passagens += 1

print(passagens)