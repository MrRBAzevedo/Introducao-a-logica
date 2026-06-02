class Triangulo:
    def __init__(self):
        self.__hight = 0
        self.__base = 0

    def set_hight(self, hight):
        self.__hight = hight

    def set_base(self, base):
        self.__base = base

    def calc_area(self):
        return self.__hight * self.__base / 2

class UserInterface:
    @staticmethod
    def main():
        a = Triangulo()

        a.set_base(float(input('Insira a base: ')))
        a.set_hight(float(input('Insira a altura: ')))

        print(a.calc_area())

UserInterface.main()