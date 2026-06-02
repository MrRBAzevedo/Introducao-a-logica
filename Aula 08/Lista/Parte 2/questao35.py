n = int(input())
ant = 0
pos = 1

for i in range(n):
    print(ant)

    pos = pos + ant
    ant = pos - ant