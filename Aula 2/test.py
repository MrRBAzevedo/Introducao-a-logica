a, b = map(int, input().split())
pilha = min(a, b)

while pilha > 0:
    if a % pilha == 0 and b % pilha == 0:
        break

    pilha -= 1

print(pilha)