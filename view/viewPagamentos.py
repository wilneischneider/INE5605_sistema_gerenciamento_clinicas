import FreeSimpleGUI as sg
from datetime import date as Date
from datetime import time as Time


class ViewPagamentos():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def init_opcoes(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("MÓDULO DE GESTÃO DE PAGAMENTOS", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Realizar Pagamento", "RD1", key="1")],
            [sg.Radio("Consultar Pagamentos", "RD1", key="2")],
            [sg.Radio("Listar Pagamentos", "RD1", key="3")],
            [sg.Radio("Consultar Saldo Devedor", "RD1", key="4")],
            [sg.Radio("Excluir Pagamento", "RD1", key="5")],
            [sg.Radio("Retornar ao Menu Inicial", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

    def view_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values["1"]:
            opcao = 1
        if values["2"]:
            opcao = 2
        if values["3"]:
            opcao = 3
        if values["4"]:
            opcao = 4
        if values["5"]:
            opcao = 5
        if values["0"] or button in (None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao

    def pegar_cpf_pagador(self):
        cpf = input("CPF do(a) Pagador(a): ")
        return cpf

    def pegar_dados_do_cartao(self):
        numero = input("Número do Cartão de Crédito: ")
        bandeira = input("Bandeira do Cartão: ")
        return {"numero": numero, "bandeira": bandeira}

    def pegar_cpf_paciente(self, pacientes: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_pacientes = []
        for cpf, nome in pacientes.items():
            lista_pacientes.append([sg.Radio(f"{nome} [CPF: {cpf}]", "RD1", key=cpf)])

        layout = [
            [sg.Text("Selecione o(a) Paciente:", font=("Helvica", 20))],
            *lista_pacientes,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            for cpf, resposta in dados.items():
                if resposta == True:
                    return cpf
                    break
        else:
            return None

    def pegar_id_pagamento(self, pagamentos: list):
        sg.change_look_and_feel("LightGrey1")
        lista_pagamentos = []
        for pagamento in pagamentos:
            id = pagamento["id"]
            lista_pagamentos.append([sg.Radio(f"Data: {pagamento["data"]}, Valor: R$"
                                              f" {pagamento["valor"]:.2f}".replace(".", ","), "RD1", key=id)])

        layout = [
            [sg.Text("Selecione o Pagamento:", font=("Helvica", 20))],
            *lista_pagamentos,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            for chave, resposta in dados.items():
                if resposta == True:
                    return chave
                    break
        else:
            return None

    def mostrar_pagamentos_paciente(self, dados: list):
        sg.change_look_and_feel("LightGrey1")
        if len(dados) > 0:
            lista_pagamentos = []
            for pagamento in dados:
                lista_pagamentos.append(f'Id: {pagamento["id"]}, Data: {pagamento["data"]}, Valor:'
                                        f' {pagamento["valor"]}\n\n')
            listagem = "".join(lista_pagamentos)

            layout = [
                [sg.Text("PAGAMENTOS DO PACIENTE", font=("Helvica", 20))],
                [sg.Text("Lista de pagamentos realizados:", font=("Helvica", 12))],
                [sg.Multiline(default_text=listagem,
                              size=(150, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum pagamento localizado!")

    def mostrar_pagamentos(self, dados: list):
        sg.change_look_and_feel("LightGrey1")
        if len(dados) > 0:
            lista_pagamentos = []
            for pagto in dados:
                lista_pagamentos.append(f'Paciente: {pagto["nome_paciente"]} [{pagto["cpf_paciente"]}], Data:'
                                        f' {pagto["data"]}, Valor: R$ {pagto["valor"]}\n\n')
            listagem = "".join(lista_pagamentos)

            layout = [
                [sg.Text("PAGAMENTOS RECEBIDOS", font=("Helvica", 20))],
                [sg.Text("Lista de pagamentos:", font=("Helvica", 12))],
                [sg.Multiline(default_text=listagem,
                              size=(150, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum pagamento localizado!")

    def mostrar_valores_em_aberto(self, dados: dict):
        sg.change_look_and_feel("LightGrey1")
        if len(dados) > 0:
            lista_atendimentos = []
            for atendimento in dados["atendimentos"]:
                lista_atendimentos.append(f'Data: {atendimento["data"]}, Horário: {atendimento["horario"]},'
                                          f' Valor do Atendimento: {atendimento["valor_atendimento"]},'
                                          f' Valor dos Procedimentos: {atendimento["valor_procedimentos"]}\n\n')
            listagem = "".join(lista_atendimentos)

            layout = [
                [sg.Text("CONSULTAR SALDO DEVEDOR", font=("Helvica", 20))],
                [sg.Text("Lista de atendimentos realizados:", font=("Helvica", 12))],
                [sg.Multiline(default_text=listagem,
                              size=(150, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Text(f'Total Pago: R$ {dados["total_pago"]:.2f}'.replace('.', ',').replace("_", "."),
                         font=("Helvica", 15))],
                [sg.Text(f'SALDO DEVEDOR: R$ {dados["saldo"]:.2f}'.replace('.', ',').replace("_", "."),
                         font=("Helvica", 15))],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum atendimento localizado!")

    def pegar_data_da_consulta(self):
        repetir = 0
        while repetir == 0:
            ano_consulta = input("Informe o Ano da Consulta (AAAA): ")
            mes_consulta = input("Informe o Mês da Consulta (MM): ")
            dia_consulta = input("Informe o Dia da Consulta (DD): ")
            try:
                ano = int(ano_consulta)
                mes = int(mes_consulta)
                dia = int(dia_consulta)
                data_consulta = Date(ano, mes, dia)
                repetir = 1
            except ValueError:
                print("Informe ano, mês e dia em numerais, nos formatos indicados. Ex.: Ano: 1990, Mês: 5, Dia: 15")
        return data_consulta

    def pegar_horario_da_consulta(self):
        repetir = 0
        while repetir == 0:
            hora_consulta = input("Informe a Hora de Início da Consulta (HH): ")
            minuto_consulta = input("Informe os Minutos de Início da Consulta (MM): ")
            try:
                hora = int(hora_consulta)
                minuto = int(minuto_consulta)
                horario_inicio = Time(hora, minuto)
                repetir = 1
            except ValueError:
                print("Informe hora e minutos em numerais, nos formatos indicados. Ex.: Hora: 18, Minuto: 27")
        return horario_inicio

    def pegar_data_de_pagamento(self):
        repetir = 0
        while repetir == 0:
            ano_pagamento = input("Informe o Ano do Pagamento (AAAA): ")
            mes_pagamento = input("Informe o Mês do Pagamento (MM): ")
            dia_pagamento = input("Informe o Dia do Pagamento (DD): ")
            try:
                ano = int(ano_pagamento)
                mes = int(mes_pagamento)
                dia = int(dia_pagamento)
                data_pagamento = Date(ano, mes, dia)
                repetir = 1
            except ValueError:
                print("Informe ano, mês e dia em numerais, nos formatos indicados. Ex.: Ano: 1990, Mês: 5, Dia: 15")
        return data_pagamento

    def pegar_valor_do_pagamento(self):
        repetir = 0
        while repetir == 0:
            valor = input("Valor do Pagamento (em R$): ")
            try:
                valor = float(valor)
                repetir = 1
            except ValueError:
                print("Informe apenas valores, utilizando ponto '.' como separador de decimal.")
        return valor

    def pegar_numero_parcelas(self):
        repetir = 0
        while repetir == 0:
            valor = input("Informe o número de parcelas: ")
            try:
                valor = int(valor)
                if valor > 0:
                    repetir = 1
                else:
                    print("Informe um valor inteiro maior que zero.")
            except ValueError:
                print("Informe um valor inteiro maior que zero.")
        return valor

    def init_opcoes_pagamento(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("MÓDULO DE GESTÃO DE PAGAMENTOS", font=("Helvica", 25))],
            [sg.Text("Selecione a Forma de Pagamento", font=("Helvica", 15))],
            [sg.Radio("Dinheiro", "RD1", key="1")],
            [sg.Radio("PIX", "RD1", key="2")],
            [sg.Radio("Cartão de Crédito", "RD1", key="3")],
            [sg.Radio("Retornar ao Menu Anterior", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

    def selecionar_forma_de_pagamento(self):
        self.init_opcoes_pagamento()
        button, values = self.open()
        if values["1"]:
            opcao = 1
        if values["2"]:
            opcao = 2
        if values["3"]:
            opcao = 3
        if values["0"] or button in (None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)
