n = int(input())
numero_cidades = 0
cidades = []
consumo_medio = []

while n != 0:
    cidade = {}
    consumo_total = 0
    habitantes = 0

    for _ in range(n):
        x, y = map(int, input().split())
        habitantes += x
        consumo_total += y
        consumo = y // x

        if consumo in cidade: cidade[consumo] += x
        else: cidade[consumo] = x

    consumo_medio.append(consumo_total / habitantes)
    cidades.append(cidade)
    numero_cidades += 1
    n = int(input())

for i in range(numero_cidades):
    ordem = sorted(cidades[i])

    print(f'Cidade# {i+1}:')
    for media in ordem:
        print(f'{cidades[i][media]}-{media}', end = ' ')
    print(f'\nConsumo médio: {consumo_medio[i]:.2f} m3.\n')

