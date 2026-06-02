a = int(input())
num = 2
soma = 0

while num <= a:
    div = 2

    while div < num:
        if num % div == 0:
            break

        div += 1
    else:
        soma += num

    num += 1

print(soma)