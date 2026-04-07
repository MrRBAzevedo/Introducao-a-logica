def maior(*args):
    maior = args[0]

    for num in args:
        if num > maior:
            maior = num

    return maior

num1 = int(input())
num2 = int(input())

print(maior(num1, num2))