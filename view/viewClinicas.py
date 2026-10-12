from view import superView
from datetime import time


class ViewClinicas(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE CLÍNICAS ---------")
        print("Escolha sua opção:")
        print("1 - Listar Clínicas")
        print("2 - Cadastrar Clínica")
        print("3 - Buscar Clínica")
        print("4 - Excluir Clínica")
        print("5 - Atualizar Nome de Clínica")
        print("6 - Atualizar Cidade de Clínica")
        print("7 - Atualizar Descrição de Clínica")
        print("8 - Corrigir CNPJ de Clínica")
        print("9 - Atualizar Horário de Abertura de Clínica")
        print("10 - Atualizar Horário de Fechamento de Clínica")
        print("11 - Listar Profissionais de Clínica")
        print("12 - Vincular Profissional à Clínica")
        print("13 - Desvincular Profissional de Clínica")
        print("0 - Retornar ao Menu Anterior")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6,7,8,9,10,11,12,13])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_dados_da_clinica(self):
        print("-------- CADASTRO DE CLÍNICA ----------")
        nome = input("Nome: ")
        cnpj = input("CNPJ: ")
        cidade = input("Cidade: ")
        descricao = input("Descrição: ")
        print("--- Horário de Funcionamento da Clínica ---")
        repetir = 0
        while repetir == 0:
            hora_abertura = input("Abertura (apenas a hora): ")
            minutos_abertura = input("Agora, os minutos: ")
            try:
                hora = int(hora_abertura)
                minuto = int(minutos_abertura)
                if 0 <= hora < 24 and 0 <= minuto < 60:
                    abertura = time(hora, minuto)
                    repetir = 1
                else:
                    print("Para horas, informe um valor inteiro entre 0 e 23")
                    print("Para minutos, informe um valor inteiro entre 0 e 59")
            except ValueError:
                print("Para horas, informe um valor inteiro entre 0 e 23")
                print("Para minutos, informe um valor inteiro entre 0 e 59")
        repetir = 0
        while repetir == 0:
            hora_fechamento = input("Fechamento (apenas a hora): ")
            minutos_fechamento = input("Agora, os minutos: ")
            try:
                hora = int(hora_fechamento)
                minuto = int(minutos_fechamento)
                if 0 <= hora < 24 and 0 <= minuto < 60:
                    fechamento = time(hora, minuto)
                    repetir = 1
                else:
                    print("Para horas, informe um valor inteiro entre 0 e 23")
                    print("Para minutos, informe um valor inteiro entre 0 e 59")
            except ValueError:
                print("Para horas, informe um valor inteiro entre 0 e 23")
                print("Para minutos, informe um valor inteiro entre 0 e 59")
        return {"nome": nome,
                "cnpj": cnpj,
                "cidade": cidade,
                "descricao": descricao,
                "horario_de_abertura": abertura,
                "horario_de_fechamento": fechamento}

    def pegar_cnpj(self):
        cnpj = input("Informe o CNPJ da Clínica: ")
        return cnpj

    def pegar_novo_nome(self):
        cnpj = input("Informe o CNPJ da Clínica: ")
        nome = input("Informe o novo nome da Clínica: ")
        return {"nome": nome, "cnpj": cnpj}

    def pegar_nova_cidade(self):
        cnpj = input("Informe o CNPJ da Clínica: ")
        cidade = input("Informe a nova cidade da Clínica: ")
        return {"cidade": cidade, "cnpj": cnpj}

    def pegar_nova_descricao(self):
        cnpj = input("Informe o CNPJ da Clínica: ")
        descricao = input("Informe a nova descrição da Clínica: ")
        return {"descricao": descricao, "cnpj": cnpj}

    def pegar_cnpj_correto(self):
        cnpj_correto = input("Informe o CNPJ correto da Clínica: ")
        cnpj_cadastrado = input("Informe o CNPJ cadastrado: ")
        return {"cnpj_correto": cnpj_correto, "cnpj_cadastrado": cnpj_cadastrado}

    def pegar_novo_horario_de_abertura(self):
        cnpj = input("Informe o CNPJ da Clínica: ")
        repetir = 0
        while repetir == 0:
            hora_abertura = input("Abertura (apenas a hora): ")
            minutos_abertura = input("Agora, os minutos: ")
            try:
                hora = int(hora_abertura)
                minuto = int(minutos_abertura)
                if 0 <= hora < 24 and 0 <= minuto < 60:
                    abertura = time(hora, minuto)
                    repetir = 1
                else:
                    print("Para horas, informe um valor inteiro entre 0 e 23")
                    print("Para minutos, informe um valor inteiro entre 0 e 59")
            except ValueError:
                print("Para horas, informe um valor inteiro entre 0 e 23")
                print("Para minutos, informe um valor inteiro entre 0 e 59")
        return {"horario_de_abertura": abertura, "cnpj": cnpj}

    def pegar_novo_horario_de_fechamento(self):
        cnpj = input("Informe o CNPJ da Clínica: ")
        repetir = 0
        while repetir == 0:
            hora_fechamento = input("Fechamento (apenas a hora): ")
            minutos_fechamento = input("Agora, os minutos: ")
            try:
                hora = int(hora_fechamento)
                minuto = int(minutos_fechamento)
                if 0 <= hora < 24 and 0 <= minuto < 60:
                    fechamento = time(hora, minuto)
                    repetir = 1
                else:
                    print("Para horas, informe um valor inteiro entre 0 e 23")
                    print("Para minutos, informe um valor inteiro entre 0 e 59")
            except ValueError:
                print("Para horas, informe um valor inteiro entre 0 e 23")
                print("Para minutos, informe um valor inteiro entre 0 e 59")
        return {"horario_de_fechamento": fechamento, "cnpj": cnpj}

    def pegar_cpf_vincular_desvincular(self):
        cnpj = input("Informe o CNPJ da Clínica: ")
        cpf = input("Informe o CPF do(a) Profissional: ")
        return {"cpf": cpf, "cnpj": cnpj}
