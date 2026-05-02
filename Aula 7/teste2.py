def soma(num1, num2):
    resultado = ''
    contador = 0
    
    while contador < len(num1):
        if num1[contador] != num2[contador]:
            resultado += '1'
        else:
            resultado += '0'

        contador += 1
    
    return resultado

x = input()
y = input()
print(soma(x, y))