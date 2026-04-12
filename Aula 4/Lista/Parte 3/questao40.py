import subprocess
subprocess.run('cls', shell = 'True')

caractere = input()

if caractere.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f'O caractere {caractere} é uma vogal')
elif len(caractere) == 1 and caractere.isalpha():
    # Método isalpha(): retorna True para uma strig que represente uma letra do alphabeto
    print(f'O caractere {caractere} é uma consoante')
elif len(caractere) == 1 and caractere.isdigit():
    # Método isdigit(): retorna True para uma strig que represente um algarismo
    print(f'O caractere {caractere} é um dígito')
else: 
    print(f'O caractere {caractere} não é uma letra ou dígito')