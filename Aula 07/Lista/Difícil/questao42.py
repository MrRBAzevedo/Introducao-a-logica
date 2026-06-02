n = int(input())
palin = []
a = 0
b = 0
c = 0

for i in range(n):
    a += 9 * 10 ** i
    b += 9 * 10 ** i
    c += 9 * 10 ** i

while a > 0:
    while b > 0:
        prod = list(str(a * b))
        
        if prod == prod[::-1]:
            palin.append(a * b)

        b -= 1
    
    b = c
    a -= 1

print(max(palin))
    

        

