contador = 1
limite = int(input())
ant = 0
post = 1

while contador <= limite:
    print(ant)

    post = post + ant
    ant = post - ant

    contador += 1