import FreeSimpleGUI as sg
from datetime import datetime
from datetime import date as Date


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
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Informe o CPF do Pagador", font=("Helvica", 20))],
            [sg.Text("CPF", size=(10, 1)), sg.InputText("", key="cpf")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["cpf"]
        else:
            return None

    def pegar_dados_do_cartao(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Informe os Dados do Cartão", font=("Helvica", 20))],
            [sg.Text("Número", size=(10, 1)), sg.InputText("", key="numero")],
            [sg.Text("Bandeira", size=(10, 1)), sg.InputText("", key="bandeira")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return {"numero": dados["numero"], "bandeira": dados["bandeira"]}
        else:
            return None

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

    def pegar_data_da_consulta(self, datas: list):
        sg.change_look_and_feel("LightGrey1")
        lista_datas = []
        for data in datas:
            lista_datas.append([sg.Radio(f"{data}", "RD1", key=data)])

        layout = [
            [sg.Text("Data da Consulta", font=("Helvica", 20))],
            [sg.Text("Selecione a data da consulta que deseja pagar:", font=("Helvica", 12))],
            *lista_datas,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            for data, resposta in dados.items():
                if resposta == True:
                    return data
                    break
        else:
            return None

    def pegar_horario_da_consulta(self, horarios: list):
        sg.change_look_and_feel("LightGrey1")
        lista_horarios = []
        for horario in horarios:
            lista_horarios.append([sg.Radio(f"{horario}", "RD1", key=horario)])

        layout = [
            [sg.Text("Horário da Consulta", font=("Helvica", 20))],
            [sg.Text("Selecione o horário da consulta que deseja pagar:", font=("Helvica", 12))],
            *lista_horarios,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            for horario, resposta in dados.items():
                if resposta == True:
                    return horario
                    break
        else:
            return None

    def pegar_data_de_pagamento(self):
        sg.change_look_and_feel("LightGrey1")
        hoje = datetime.now()
        hoje_formatado = hoje.strftime("%Y-%m-%d")
        layout = [
            [sg.Text("Informe a Data de Pagamento", font=("Helvica", 20))],
            [
                sg.Text("Data:", size=(7, 1)),
                sg.InputText(hoje_formatado, key="data", size=(20, 1), readonly=True),
                sg.CalendarButton(
                    "Selecione a data",
                    target="data",
                    format="%Y-%m-%d",
                    close_when_date_chosen=True
                )
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados_bruto = values
        self.close()
        if button is not None and button == "Confirmar":
            return Date.strptime(dados_bruto['data'], "%Y-%m-%d")
        else:
            return None

    def pegar_valor_do_pagamento(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Informe o valor que deseja Pagar", font=("Helvica", 20))],
            [sg.Text("Valor (R$):", size=(10, 1)), sg.InputText("", key="valor")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                valor = float(dados["valor"])
                return valor
            except ValueError:
                sg.popup("Informe apenas números e utilize ponto '.' como separador de decimal.")
                return None
        else:
            return None

    def pegar_numero_parcelas(self):
        sg.change_look_and_feel("LightGrey1")
        parcelas = [f"{h}" for h in range(1, 7)]
        layout = [
            [sg.Text("Informe o número de parcelas", font=("Helvica", 20))],
            [
                sg.Text("Número de parcelas:", size=(20, 1)),
                sg.Spin(parcelas, initial_value=1, key="valor", size=(3, 1), readonly=True),
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pagamentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return int(dados["valor"])
        else:
            return None

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
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            if True in dados.values():
                for opcao, resposta in dados.items():
                    if resposta == True:
                        return int(opcao)
                        break
            else:
                return 0
        else:
            return 0

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)
