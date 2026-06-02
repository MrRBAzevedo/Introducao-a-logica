n1 = int(input())
n2 = int(input())
dv = max(n1, n2)
ds = min(n1, n2)

for i in iter(int, 1):
    if dv % ds == 0:
        print(f'MDC{n1, n2}: {ds}')
        break
    else:
        x = dv % ds
        dv = ds
        ds = x