x = float(input())
H = 0
den = 0

while H <= x:
    den += 1
    H += 1 / den

print(den)
print(H)