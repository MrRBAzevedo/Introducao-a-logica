n = int(input())
exp = 0

while 2 ** exp <= n:
    print(2 ** exp)
    exp += 1