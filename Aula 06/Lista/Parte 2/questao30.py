num = int(input())
div = 2

while div < num:
    if num % div == 0:
        print('O número não é primo')
        break
    
    div += 1
else:
    print('O número é primo')