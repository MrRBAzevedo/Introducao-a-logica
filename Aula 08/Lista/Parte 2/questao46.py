n = int(input())
valores = []

for i in range(n):
    valor = float(input())
    valores.append(valor)

for valor in valores:
    if valor < 10:
        print(f'{valor} pequeno')
    elif valor <= 100:
        print(f'{valor} médio')
    else:
        print(f'{valor} grande')
