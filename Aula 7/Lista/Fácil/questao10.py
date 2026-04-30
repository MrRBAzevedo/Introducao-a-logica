n = int(input())
contador = 1
ant = 0
pos = 1

while contador <= n:
    print(ant)

    pos = ant + pos
    ant = pos - ant
    contador += 1