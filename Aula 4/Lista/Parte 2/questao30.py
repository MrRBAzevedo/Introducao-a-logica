string = input('Insira uma string: ')

print(string.upper() if len(string) > 5 else string.lower())