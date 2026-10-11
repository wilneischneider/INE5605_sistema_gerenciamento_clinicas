from controller.controllerPacientes import ControllerPaciente
from datetime import date as Date


class ViewPacientes:
    def opcoes_paciente(self):
        print("-------- PACIENTES ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Paciente")
        print("2 - Excluir Paciente")
        print("3 - Listar ")
        print("4 - Excluir Amigo")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
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