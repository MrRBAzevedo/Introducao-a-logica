A = input().strip()
B = input().strip()

# Faz os dois números terem o mesmo tamanho
n = max(len(A), len(B))
A = A.zfill(n)
B = B.zfill(n)

resA = []
resB = []

# Compara os dígitos da direita para a esquerda
for i in range(n - 1, -1, -1):
    if A[i] > B[i]:
        resA.append(A[i])
    elif A[i] < B[i]:
        resB.append(B[i])
    else:
        resA.append(A[i])
        resB.append(B[i])

# Inverte para restaurar a ordem original
resA.reverse()
resB.reverse()

def trata(numero):
    s = "".join(numero).lstrip("0")
    return "-1" if s == "" else s

resA = trata(resA)
resB = trata(resB)

# Imprime em ordem não decrescente
if resA == "-1" and resB == "-1":
    print("-1 -1")
elif resA == "-1":
    print("-1", resB)
elif resB == "-1":
    print("-1", resA)
else:
    if int(resA) <= int(resB):
        print(resA, resB)
    else:
        print(resB, resA)