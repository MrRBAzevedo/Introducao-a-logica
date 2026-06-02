num = int(input())
divs = []
div = 1

while True:
    if div in divs:
        break
    elif num % div == 0:
        divs.append(div)
        divs.append(num/div)

    div += 1

print(len(divs))