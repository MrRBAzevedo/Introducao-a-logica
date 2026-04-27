num = int(input())
dig = 0
exp = 0

while True:
    if num // 10 ** exp == 0:
        break
    else:
        dig += 1
    
    exp += 1

print(dig)
