a = input()
b = input()
tam_a = len(a)
tam_b = len(b)
maior = max(tam_a, tam_b)
dif = abs(tam_a - tam_b)

if tam_a > tam_b:
    b = '0' * dif + b
elif tam_b > tam_a:
    a = '0' * dif + a

resultado_a = []
resultado_b = []

for i in range(maior):
    if a[i] > b[i]:
        resultado_a.append(a[i])
    elif b[i] > a[i]:
        resultado_b.append(b[i])
    else:
        resultado_a.append(a[i])
        resultado_b.append(b[i])

num_a = int(''.join(resultado_a)) if resultado_a else -1
num_b = int(''.join(resultado_b)) if resultado_b else -1

print(f'{num_a} {num_b}' if num_b > num_a else f'{num_b} {num_a}')