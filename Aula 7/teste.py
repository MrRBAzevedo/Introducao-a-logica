def maior(*args):
    m = args[0]

    for num in args:
        if num > m:
            m = num

    return m

num = maior(10, 20, 30, 40, 50, 60, 70)
print(num)