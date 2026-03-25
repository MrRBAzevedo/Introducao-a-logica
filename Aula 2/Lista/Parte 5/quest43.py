import subprocess

class Retangulo:
    def __init__(self):
        self.__base = 1
        self.__altura = 1

    def set_base(self, base):
        if base > 0:
            self.__base = base
        else:
            raise ValueError('A base não pode possuir um valor nulo ou negativo.')
        
    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError('A altura não pode possuir um valor nulo ou negativo.')
        
    def calc_area(self):
        return self.__base * self.__altura
    
class UserInterface:
    @staticmethod
    def main():
        subprocess.run(['cls'], shell = True)
        x = Retangulo()

        base = int(input('Insira o valor da base: '))
        x.set_base(base)
        altura = int(input('Insira o valor da altura: '))
        x.set_altura(altura)

        print(f'A área do retângulo é: {x.calc_area()}')

UserInterface.main()