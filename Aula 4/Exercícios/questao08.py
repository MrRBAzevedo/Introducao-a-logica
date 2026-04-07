idade = int(input())

if idade < 5:
    print('Sem categoria')
elif idade <= 7:
    print('Peixinho')
elif idade <= 10:
    print('Infantil A')
elif idade <= 13:
    print('Infantil B')
elif idade <= 17:
    print('Juvenil')
else:
    print('Adulto')