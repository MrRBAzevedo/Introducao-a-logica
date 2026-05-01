V = int(input('Insira o valor em centavos: '))
moedas = input('Insira as denominações disponíveis: ').split()
moedas = [int(moeda) for moeda in moedas]
moedas.sort(reverse = True)
contador = 0

while contador < len(moedas):
    moeda = moedas[contador]
    print(f'{V // moeda} {'moedas' if V // moeda > 1 else 'moeda'} de {moeda} centavos')

    V = V % moedas[contador]

    contador += 1