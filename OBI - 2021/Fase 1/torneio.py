jogos = []
for i in range(6):
    jogo = input()
    jogos.append(jogo)

vitorias = jogos.count('V')

if vitorias >= 5:
    print(1)
elif vitorias >= 3:
    print(2)
elif vitorias >= 1:
    print(3)
else:
    print(-1)