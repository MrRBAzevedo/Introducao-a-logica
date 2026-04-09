class Idade:
    def __init__(self):
        self.__nascimento = {'dia' : 1, 'mes' : 1, 'ano' : 1}
        self.__dia = {'dia' : 1, 'mes' : 1, 'ano' : 1}

    def set_dia(self, dia):
        if dia[0] > 0:
            self.__dia['dia'] = dia[0]
        else:
            raise ValueError('Valor inválido')
        
        if dia[1] > 0:
            self.__dia['mes'] = dia[1]
        else:
            raise ValueError('Valor inválido')

        if dia[2] > 0:
            self.__dia['ano'] = dia[2]
        else:
            raise ValueError('Valor inválido')
        
    def show_dia(self):
        return f'{self.__dia['dia']}/{self.__dia['mes']}/{self.__dia['ano']}'

a = Idade()

dia = list(map(int, input('Insira o dia (dd/mm/aaaa): ').split('/')))
a.set_dia(dia)

print(a.show_dia())