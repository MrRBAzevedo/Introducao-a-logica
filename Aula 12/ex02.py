import enum
from datetime import datetime, timedelta

class SituacaoEstagio(enum.Enum):
    Cadastrado = 1
    Iniciado = 2
    Cancelado = 3
    Finalizado = 4

class Estagio:
    def __init__(self, est, emp):
        self.set_estagiario(est)
        self.set_empresa(emp)
        self.__data_inicio = None
        self.__data_cancelamento = None
        self.__data_fim = None
        self.__situacao = SituacaoEstagio.Cadastrado
        

    def set_estagiario(self, est):
        if est: self.__estagiario = est
        else: raise ValueError("Estagiário deve ser informado")
    def set_empresa(self, emp):
        if emp: self.__empresa = emp
        else: raise ValueError("Empresa deve ser informada")
    def get_estagiario(self): return self.__estagiario
    def get_empresa(self): return self.__empresa
    def get_situacao(self): return self.__situacao

    def iniciar(self, data):
        if self.__situacao != SituacaoEstagio.Cadastrado:
            raise ValueError("Só é possível iniciar um estágio cadastrado")
        self.__data_inicio = data
        self.__situacao = SituacaoEstagio.Iniciado

    def cancelar(self, data):
        if self.__situacao != SituacaoEstagio.Finalizado:
            raise ValueError("Só é possível cancelar um estágio não finalizado")
        self.__data_cancelamento = data
        self.__situacao = SituacaoEstagio.Cancelado

    def finalizar(self, data):
        if self.__situacao != SituacaoEstagio.Iniciado: 
            raise ValueError("Só é possível finalizar um estágio iniciado")       
        
        self.__data_fim = data
        self.__situacao = SituacaoEstagio.Finalizado


    def tempo_estagio(self):
        if self.__situacao == SituacaoEstagio.Cadastrado:
            return timedelta()
        elif self.__situcao == SituacaoEstagio.Iniciado:
            return datetime.now() - self.__data_inicio
        elif self.__situacao == SituacaoEstagio.Cancelado:
            return self.__data_cancelamento - self.__data_inicio
        else:
            return self.__data_fim - self.__data_inicio

    def __str__(self):
        s = f"{self.__estagiario} - {self.__empresa}"
        if self.__situacao == SituacaoEstagio.Cadastrado:
            return s + " - aguardando início"
        elif self.__situacao == SituacaoEstagio.Iniciado:
            return s + f" - iniciado em {self.__data_inicio.strftime('%d/%m/%Y')}"
        elif self.__situacao == SituacaoEstagio.Cancelado:
            return s + f" - cancelado em {self.__data_cancelamento.strftime('%d/%m/%Y')}"
        else:
            return s + f" - realizado no período {self.__data_inicio.strftime('%d/%m/%Y')} a {self.__data_fim.strtime('%d/%m/%Y')}"

# class UserInterface:
#     @staticmethod
#     def main():
#         op = 0
#         while op != 9:
#             if op == 1: UserInterface.inserir()
#             elif op == 2: UserInterface.listar_empresa()

#     @staticmethod
#     def menu():
#         print("1 - Inserir, 2 - Listar ordenado por empresa, 9 - Fim")
#         return int(input("Informe a opção: "))

#     @classmethod
#     def inserir(cls):
#         estagiario = input("Informe o nome do estagiário: ")
#         empresa = input("Informe o nome da empresa: ")
#         a = Estagio(estagiario, empresa)
#         cls.estagios.append(a)

    


# estagio01 = Estagio("Pedro", "IFRN")
# estagio02 = Estagio("Lucas", "UFRN")
# estagio03 = Estagio("Danielle", "INSS")
# estagio04 = Estagio("Marília", "Serpro")

# estagio01.iniciar(datetime(2026, 6, 5))
# estagio02.iniciar(datetime(2026, 7, 12))

# print(estagio01)
# print(estagio02)
# print(estagio03)
# print(estagio04)
        
