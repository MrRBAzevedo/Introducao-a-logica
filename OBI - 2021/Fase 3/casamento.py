a = int(input())
b = int(input())
repeticoes = len(list(str(max(a, b))))
resultado_a = ''
resultado_b = ''

for i in range(repeticoes):
    digito_a = a % 10
    a //= 10
    digito_b = b % 10
    b //= 10

    if digito_a > digito_b:
        resultado_a = str(digito_a) + resultado_a
    elif digito_b > digito_a:
        resultado_b = str(digito_b) + resultado_b
    else:
        resultado_a = str(digito_a) + resultado_a
        resultado_b = str(digito_b) + resultado_b

resultado_a = int(resultado_a) if resultado_a else -1
resultado_b = int(resultado_b) if resultado_b else -1

print(f'{resultado_a} {resultado_b}' if resultado_a < resultado_b else f'{resultado_b} {resultado_a}')


