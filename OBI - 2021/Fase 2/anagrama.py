# def Listar(vetor):
#     lista = []
#     for caractere in vetor:
#         if caractere not in [' ', '.', ',']:
#             lista.append(caractere)

#     return lista

# n = int(input())
# a = input()
# b = input()

# lista_a = Listar(a)
# lista_b = Listar(b)

# letras = {}

# for i in range(n):
#     if lista_a[i] in letras:
#         letras[lista_a[i]] += 1
#     else:
#         letras[lista_a[i]] = 1

#     if lista_b[i] in letras:
#         letras[lista_b[i]] -= 1
#     else:
#         letras[lista_b[i]] = -1

# print(letras)


n = int(input())
a = list(input())
b = list(input())
letras = {}

for i in range(n):
    if a[i] not in [' ', ',', '.']:
        if a[i] in letras:
            letras[a[i]] += 1
        else:
            letras[a[i]] = 1
    
    if b[i] not in [' ', ',', '.']:
        if b[i] in letras:
            letras[b[i]] -= 1
        else:
            letras[b[i]] = -1
    
for letra in letras:
    if letras[letra] != 0:
        print('N')
        break
else:
    print('S')