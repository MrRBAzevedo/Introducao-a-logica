n = int(input())

def Rec(num):
    if num == 0:
        return 2
    else:
        anterior = Rec(num - 1)
        return 2 * anterior - 1

print(Rec(n) ** 2)