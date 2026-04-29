def maior(*args):
    maior = args[0]

    for num in args:
        if num > maior:
            maior = num

    return maior


x, y, z = map(int, input().split())
print(maior(x, y, z))