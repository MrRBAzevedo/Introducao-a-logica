import math

m = int(input()) - 1
n = int(input()) - 1
total = m + n

pos = math.factorial(total) // (math.factorial(m) * math.factorial(n))

print(pos)
