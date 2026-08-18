n, f = map(int, input().split())
c = list(map(int, input().split()))

def Contar(dias):
    global c
    moedas = 0

    for capsula in c:
        moedas += dias // capsula

    return moedas

maior = 10**8
menor = 1
meio = (maior + menor) // 2

while menor < maior:
    meio = (maior + menor) // 2
    
    if Contar(meio) >= f:
        maior = meio
    else:
        menor = meio + 1

print(menor)
