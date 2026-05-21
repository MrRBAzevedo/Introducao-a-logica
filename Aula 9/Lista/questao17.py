def divisao(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor

    return (quociente, resto)

def main():
    dividendo = int(input())
    divisor = int(input())

    