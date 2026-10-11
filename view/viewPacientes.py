from controller.controllerPacientes import ControllerPaciente
from datetime import date as Date
from view import superView


class ViewPacientes(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE PACIENTES ---------")
        print("Escolha sua opção:")
        print("1 - Gerenciar Atendimentos")
        print("2 - Gerenciar Pagamentos")
        print("3 - Gerenciar Pacientes")
        print("4 - Gerenciar Procedimentos")
        print("5 - Gerenciar Profissionais")
        print("6 - Gerenciar Clínicas")
        print("0 - Finalizar sistema")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6])
        return opcao

    def solicitar_dados_paciente(self):
        print("-------- DADOS DO PACIENTE ----------")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        ano_de_nascimento = input("Ano de Nascimento: ")
        mes_de_nascimento = input("Mês de Nascimento: ")
        dia_de_nascimento = input("Dia de Nascimento: ")
        data_de_nascimento = Date(ano_de_nascimento, mes_de_nascimento, dia_de_nascimento)
        return {"nome": nome, "celular": celular, "cpf": cpf, "data_de_nascimento": data_de_nascimento}

    def mostrar_dados_paciente(self, dados_amigo):
        print("Nome: ", dados_amigo["nome"])
        print("Celular: ", dados_amigo["telefone"])
        print("CPF: ", dados_amigo["cpf"])
        print("Data de Nascimento: ", dados_amigo["cpf"])
        print("\n")

    def seleciona_amigo(self):
        cpf = input("CPF do amigo que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)