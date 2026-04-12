l1 = float(input('Insira o primeiro lado: '))
l2 = float(input('Insira o segundo lado: '))
l3 = float(input('Insira o terceiro lado: '))

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('O triâgulo é equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Esse valores não formam um triângulo')