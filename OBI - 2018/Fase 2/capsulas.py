def Dias(C, F):
    dia = 0
    moedas = 0

    while moedas < F:
        mmc = True
        dia += 1
        
        for capsula in C:
            if dia % capsula == 0:
                moedas += 1
            else:
                mmc = False

        if mmc:
            break

    return dia, moedas

N, F = map(int, input().split())
C = list(map(int, input().split()))

dia, moedas = Dias(C, F)

if moedas >= F:
    print(dia)
else:
    dias = F // moedas * dia

    dias += Dias(C, F % moedas)[0]

    print(dias)
