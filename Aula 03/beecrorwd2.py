hi, mi, hf, mf = map(int, input().split())

if hf < hi:
    hf += 24
elif hf == hi and mf <= mi:
    hf += 24

if mf < mi:
    hf -= 1
    mf += 60

h = hf - hi
m = mf - mi

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')