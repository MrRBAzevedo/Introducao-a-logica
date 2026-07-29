a = input()
b = input()
tamanho_a = len(a)
tamanho_b = len(b)
tamanho = max(tamanho_a, tamanho_b)

if tamanho_a > tamanho_b:
    b = (tamanho_a - tamanho_b) * '0' + b
elif tamanho_b > tamanho_a:
    a = (tamanho_b - tamanho_a) * '0' + a

resul_a = []
resul_b = []

for i in range(tamanho -1, -1, -1):
    if a[i] > b[i]:
        resul_a.append(a[i])
    elif b[i] > a[i]:
        resul_b.append(b[i])
    else:
        resul_a.append(a[i])
        resul_b.append(b[i])

resul_a.reverse()
resul_b.reverse()

resul_a = int(''.join(resul_a)) if resul_a else -1
resul_b = int(''.join(resul_b)) if resul_b else -1

print(f'{resul_a} {resul_b}' if resul_b > resul_a else f'{resul_b} {resul_a}')

