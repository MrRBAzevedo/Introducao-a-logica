num = int(input())
div = 2

while div < num:
    if num % div == 0:
        print(f'O número {num} não é primo')
        break

    div += 1
else:
    print(f'O número {num} é primo')