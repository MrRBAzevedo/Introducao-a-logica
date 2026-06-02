for n in range(1000):
    soma = 0

    for div in range(1, n):
        if n % div == 0:
            soma += div

    if n == soma:
        print(f'{n} é perfeito')
    else:
        print(f'{n} não é perfeito')