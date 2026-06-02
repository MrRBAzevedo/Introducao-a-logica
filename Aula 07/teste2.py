class Triangulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0

    def set_base(self, base):
        self.__b = base

    def set_hight(self, hight):
        self.__h = hight

    def calc_area(self):
        return self.__b * self.__h / 2

a = Triangulo()
a.set_base(20)
a.set_hight(10)
print(a.calc_area())