from datetime import date as Date
from view.superView import SuperView


class ViewPacientes(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE PACIENTES ---------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Paciente")
        print("2 - Buscar Paciente")
        print("3 - Listar Pacientes")
        print("4 - Excluir Paciente")
        print("5 - Atualizar Nome do(a) Paciente")
        print("6 - Atualizar Celular do(a) Paciente")
        print("7 - Corrigir Data de Nascimento do(a) Paciente")
        print("8 - Corrigir CPF do(a) Paciente")
        print("0 - Retornar")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6,7,8])
        return opcao

    def pegar_dados_paciente(self):
        print("-------- CADASTRO DE PACIENTE ----------")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        repetir = 0
        while repetir == 0:
            ano_de_nascimento = input("Ano de Nascimento (AAAA): ")
            mes_de_nascimento = input("Mês de Nascimento (MM): ")
            dia_de_nascimento = input("Dia de Nascimento (DD): ")
            try:
                ano = int(ano_de_nascimento)
                mes = int(mes_de_nascimento)
                dia = int(dia_de_nascimento)
                data_de_nascimento = Date(ano, mes, dia)
                repetir = 1
            except ValueError:
                print("Informe ano, mês e dia em numerais, nos formatos indicados. Ex.: Ano: 1990, Mês: 5, Dia: 15")
        return {"nome": nome, "celular": celular, "cpf": cpf, "data_de_nascimento": data_de_nascimento}

    def mostrar_dados_paciente(self, lista_dados:list):
        print("--- PACIENTE(S) CADASTRADO(S) ---")
        if len(lista_dados) > 0:
            for dados_paciente in lista_dados:
                print("Nome: ", dados_paciente["nome"])
                print("Celular: ", dados_paciente["celular"])
                print("CPF: ", dados_paciente["cpf"])
                print("Data de Nascimento: ", dados_paciente["data_de_nascimento"])
                print("--------------------------------")
        else:
            print("Nenhum paciente encontrado!")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_cpf(self):
        cpf = input("Informe o CPF do(a) Paciente: ")
        return cpf

    def pegar_novo_nome(self):
        cpf = input("Informe o CPF do(a) Paciente: ")
        nome = input("Informe o novo nome do(a) Paciente: ")
        return {"nome": nome, "cpf": cpf}

    def pegar_novo_celular(self):
        cpf = input("Informe o CPF do(a) Paciente: ")
        celular = input("Informe o novo celular do(a) Paciente: ")
        return {"celular": celular, "cpf": cpf}

    def pegar_data_de_nascimento(self):
        cpf = input("Informe o CPF do(a) Paciente: ")
        repetir = 0
        while repetir == 0:
            ano_de_nascimento = input("Ano de Nascimento (AAAA): ")
            mes_de_nascimento = input("Mês de Nascimento (MM): ")
            dia_de_nascimento = input("Dia de Nascimento (DD): ")
            try:
                ano = int(ano_de_nascimento)
                mes = int(mes_de_nascimento)
                dia = int(dia_de_nascimento)
                data_de_nascimento = Date(ano, mes, dia)
                repetir = 1
            except ValueError:
                print("Informe ano, mês e dia em numerais, nos formatos indicados. Ex.: Ano: 1990, Mês: 5, Dia: 15")
        return {"data_de_nascimento": data_de_nascimento, "cpf": cpf}

    def pegar_cpf_correto(self):
        cpf_correto = input("Informe o CPF correto do(a) Paciente: ")
        cpf_cadastrado = input("Informe o CPF cadastrado: ")
        return {"cpf_correto": cpf_correto, "cpf_cadastrado": cpf_cadastrado}
