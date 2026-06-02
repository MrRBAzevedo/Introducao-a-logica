num = int(input())
pert = 'pertence' if 0 <= num <= 6 else 'não pertence'
print(f'{num} {pert} ao intervalo [0, 6]')