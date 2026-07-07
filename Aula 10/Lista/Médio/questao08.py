n, s = map(int, input().split())
lista = list(map(int, input().split()))
dicio = {}

for i, valor in enumerate(lista):
    fator = s - valor

    if fator in dicio:
        print(dicio[fator], i)
        break

    dicio[valor] = i
else:
    print('-1 -1')








# for i, valor in enumerate(lista):
#     dicio[valor] = i

# for valor, i in dicio.items():
#     fator = s - valor

#     if fator in dicio:
#         if i < dicio[fator]:
#             print(i, dicio[fator])
#             break
# else:
#     print('-1 -1')
