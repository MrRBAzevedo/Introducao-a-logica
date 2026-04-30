a = int(input())
b = int(input())
mdc = b

while a % mdc != 0:
    mdc = a % mdc
    a = b
    b = mdc

print(mdc)