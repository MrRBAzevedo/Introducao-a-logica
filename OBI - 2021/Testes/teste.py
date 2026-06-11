P = int(input())
O = int(input())
cafes = 0

for p in range(1, P+1):
    for o in range(1, O+1):
        if o % 2 == 0 and p% 2 == 0:
            if o / p ==  2:
                cafes += 1
print(cafes)