resposta = 0
s = int(input())
a = int(input())
b = int(input())

while a <= b:
    lista_string = list(str(a))
    lista_int = [int(item) for item in lista_string]
    soma = sum(lista_int)

    if soma == s:
        resposta += 1

    a += 1

print(resposta)
