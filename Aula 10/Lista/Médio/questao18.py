from collections import deque

q = int(input())
fila = deque()

for i in range(q):
    operando = input().split()

    if operando[0] == 'SAI':
        fila.popleft()
    else:
        fila.append(int(operando[1]))

print(*fila)
