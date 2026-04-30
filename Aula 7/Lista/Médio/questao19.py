n = int(input())
bin = []

if n == 0: print(n)
while n != 0:
    bin.append(n % 2)
    n //= 2

bin.reverse()

for dig in bin:
    print(dig, end = '')