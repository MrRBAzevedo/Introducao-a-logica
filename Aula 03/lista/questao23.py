A = 4
B = 10
C = 4
D = True
E = False
F = 0
G = -3
I = [1, 2, 3, 4, 5]

print(D and B or A)
# Primeiramente será avaliado o operador and, que retornará B, pois não há valores falsos e B é o último
# Em seguida, será avaliado o operador or, que retornará B, pois é o primeiro valor True encontrado

D = False
print(D and B or A)
# Primeiramente, será avaliado o operador and, que retornará D, pois é o primeiro valor falso encontrado
# Em seguida, será avaliado o operador or, que retornará A, pois é o primeiro valor True encontrado


