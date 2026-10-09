from ex02 import Estagio, SituacaoEstagio
from datetime import datetime, timedelta

class UserInterface:
    estagios = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UserInterface.menu()
            if op == 1: UserInterface.inserir()
            elif op == 2: UserInterface.listar_empresa()
            elif op == 3: UserInterface.listar_estagiario()
            elif op == 4: UserInterface.filtrar_situacao()
            elif op == 5: UserInterface.iniciar_estagio()

    @staticmethod
    def menu():
        print("1 - Inserir, 2 - Listar ordenado por empresa, 3 - Listar por estágio, 4 - Filtrar Situação, 5 - Iniciar estágio, 9 - Fim")
        return int(input("Informe a opção: "))

    @classmethod
    def inserir(cls):
        estagiario = input("Informe o nome do estagiário: ")
        empresa = input("Informe o nome da empresa: ")
        a = Estagio(estagiario, empresa)
        cls.estagios.append(a)

    @classmethod
    def listar_empresa(cls):
        cls.estagios.sort(key = lambda a : a.get_empresa() + a.get_estagiario())
        for a in cls.estagios:
            print(a)

    @classmethod
    def listar_estagiario(cls):
        cls.estagios.sort(key = lambda a : a.get_estagiario() + a.get_empresa())
        for a in cls.estagios:
            print(a)

    @classmethod
    def filtrar_situacao(cls):
        op = int(input("Informe a situação: 1 - Cadastrado, 2 - Iniciado, 3 - Cancelado, 4 - Finalizado"))
        estagios_em_situacao = []
        for a in cls.estagios:
            if a.get_situacao() == SituacaoEstagio(op):
                estagios_em_situacao.append(a)
        for a in estagios_em_situacao:
            print(a)


    @classmethod
    def iniciar_estagio(cls):
        for i, a in enumerate(cls.estagios):
            if a.get_situacao() == SituacaoEstagio.Cadastrado:
                print(f"{i}: {a}")
        op = int(input("Informe o número do estágio para iniciar: "))
        cls.estagios[op].iniciar(datetime.now())
        pass


UserInterface.main()