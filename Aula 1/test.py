import subprocess

class User:
    def __init__(self):
        self.__nome = ''
    
    def set_nome(self, nome):
        self.__nome = nome

    def __str__(self):
        return self.__nome

class Interface:
    @staticmethod
    def main():
        subprocess.run(['cls'], shell = True)
        me = User()

        nome = input('Insira seu nome: ')
        me.set_nome(nome)

        print(f'\nSeja bem vindo, {me}!')

Interface.main()




        