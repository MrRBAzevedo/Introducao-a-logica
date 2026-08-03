import math

A = int(input())
S = int(input())
D = int(input())

A -= S
dias = 1

dias += math.ceil(A / (S - D))

print(dias)
