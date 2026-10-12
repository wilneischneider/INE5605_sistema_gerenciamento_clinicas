from view import superView
from datetime import date as Date
from datetime import time as Time


class ViewAtendimentos(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE ATENDIMENTOS ---------")
        print("Escolha sua opção:")
        print("1 - Agendar Atendimento")
        print("2 - Registrar Procedimento")
        print("3 - Consultar Atendimento")
        print("4 - Cancelar Atendimento")
        print("0 - Finalizar sistema")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_dados_do_responsavel(self):
        print("!!! PACIENTE MENOR DE 18 ANOS NA DATA DA CONSULTA !!!")
        print("Necessário acompanhamento de Responsável!")
        print("--- Dados do Responsável ---")
        nome = input("Informe o nome do Responsável: ")
        celular = input("Informe o número de celular do Responsável: ")
        cpf = input("Informe o CPF do Responsável: ")
        return {"nome": nome, "celular": celular, "cpf": cpf}

    def pegar_dados_agendar_atendimento(self):
        print("-------- AGENDAMENTO DE ATENDIMENTO ----------")
        cnpj = input("CNPJ da Clínica do Atendimento: ")
        cpf_paciente = input("CPF do Paciente: ")
        cpf_profissional = input("CPF do Profissional: ")
        tipo_de_atendimento = input("Tipo de Atendimento desejado: ")
        repetir = 0
        while repetir == 0:
            ano_consulta = input("Ano da Consulta (AAAA): ")
            mes_consulta = input("Mês da Consulta (MM): ")
            dia_consulta = input("Dia da Consulta (DD): ")
            try:
                ano = int(ano_consulta)
                mes = int(mes_consulta)
                dia = int(dia_consulta)
                data = Date(ano, mes, dia)
                repetir = 1
            except ValueError:
                print("Informe ano, mês e dia em numerais, nos formatos indicados. Ex.: Ano: 1990, Mês: 5, Dia: 15")
        repetir = 0
        while repetir == 0:
            hora_consulta = input("Hora de Início da Consulta (HH): ")
            minuto_consulta = input("Minutos de Início da Consulta (MM): ")
            try:
                hora = int(hora_consulta)
                minuto = int(minuto_consulta)
                horario_inicio = Time(hora, minuto)
                repetir = 1
            except ValueError:
                print("Informe hora e minutos em numerais, nos formatos indicados. Ex.: Hora: 18, Minuto: 27")
        repetir = 0
        while repetir == 0:
            hora_consulta = input("Hora de Fim da Consulta (HH): ")
            minuto_consulta = input("Minutos de Fim da Consulta (MM): ")
            try:
                hora = int(hora_consulta)
                minuto = int(minuto_consulta)
                horario_fim = Time(hora, minuto)
                repetir = 1
            except ValueError:
                print("Informe hora e minutos em numerais, nos formatos indicados. Ex.: Hora: 18, Minuto: 27")
        repetir = 0
        while repetir == 0:
            valor = input("Valor do Atendimento (em R$): ")
            try:
                valor = float(valor)
                repetir = 1
            except ValueError:
                print("Informe apenas valores, utilizando ponto '.' como separador de decimal.")
        return {"cnpj": cnpj, "cpf_paciente": cpf_paciente, "cpf_profissional": cpf_profissional,
                "data": data, "horario_inicio": horario_inicio, "horario_fim": horario_fim,
                "tipo_de_atendimento": tipo_de_atendimento, "valor": valor}
