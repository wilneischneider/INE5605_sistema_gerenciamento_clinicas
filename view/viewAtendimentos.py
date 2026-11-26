from datetime import date as Date
from datetime import time as Time
import FreeSimpleGUI as sg


class ViewAtendimentos():
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
            [sg.Text("MÓDULO DE GESTÃO DE ATENDIMENTOS", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Agendar Atendimento", "RD1", key="1")],
            [sg.Radio("Registrar Procedimento", "RD1", key="2")],
            [sg.Radio("Consultar Atendimento", "RD1", key="3")],
            [sg.Radio("Excluir Atendimento", "RD1", key="4")],
            [sg.Radio("Listar Atendimentos", "RD1", key="5")],
            [sg.Radio("Retornar ao Menu Inicial", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

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

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def pegar_dados_do_responsavel(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("PACIENTE MENOR DE 18 ANOS NA DATA DA CONSULTA", font=("Helvica", 25))],
            [sg.Text("Necessário acompanhamento de Responsável!", font=("Helvica", 12))],
            [sg.Text("Dados do Responsável", font=("Helvica", 15))],
            [sg.Text("Nome do(a) Responsável", size=(37, 1)), sg.InputText("", key="nome")],
            [sg.Text("Número do Celular do(a) Responsável", size=(37, 1)), sg.InputText("", key="celular")],
            [sg.Text("CPF do(a) Responsável", size=(37, 1)), sg.InputText("", key="cpf")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados
        else:
            return None

    def pegar_clinica(self, clinicas: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_clinicas = []
        for chave, valor in clinicas.items():
            lista_clinicas.append([sg.Radio(f"{valor.nome} - {valor.cidade}", "RD1", key=chave)])

        layout = [
            [sg.Text("SELEÇÃO DE CLÍNICA", font=("Helvica", 25))],
            [sg.Text("Selecione a clínica desejada:", font=("Helvica", 20))],
            *lista_clinicas,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        for chave, valor in values.items():
            if valor == True:
                dados = chave
                break
        self.close()
        if button is not None and button == "Confirmar":
            return dados
        else:
            return None

    def pegar_profissional(self, profissionais: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_profissionais = []
        for chave, valor in profissionais.items():
            lista_profissionais.append([sg.Radio(f"{valor.nome} - {valor.especialidade}", "RD1", key=chave)])

        layout = [
            [sg.Text("SELEÇÃO DE PROFISSIONAL", font=("Helvica", 25))],
            [sg.Text("Selecione o(a) profissional desejado(a):", font=("Helvica", 20))],
            *lista_profissionais,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        for chave, valor in values.items():
            if valor == True:
                dados = chave
                break
        self.close()
        if button is not None and button == "Confirmar":
            return dados
        else:
            return None

    def pegar_tipo_atendimento(self, tipos_atendimento: list):
        sg.change_look_and_feel("LightGrey1")
        lista_tipos_atendimento = []
        for tipo in tipos_atendimento:
            lista_tipos_atendimento.append([sg.Radio(f"{tipo}", "RD1", key=tipo)])

        layout = [
            [sg.Text("SELEÇÃO DE TIPO DE ATENDIMENTO", font=("Helvica", 25))],
            [sg.Text("Selecione o tipo de atendimento desejado:", font=("Helvica", 20))],
            *lista_tipos_atendimento,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        for chave, valor in values.items():
            if valor == True:
                dados = chave
                break
        self.close()
        if button is not None and button == "Confirmar":
            return dados
        else:
            return None

    def pegar_paciente(self, pacientes: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_pacientes = []
        for chave, valor in pacientes.items():
            lista_pacientes.append([sg.Radio(f"{valor.nome} [CPF: {valor.cpf}]", "RD1", key=chave)])

        layout = [
            [sg.Text("SELEÇÃO DE PACIENTE", font=("Helvica", 25))],
            [sg.Text("Selecione o(a) paciente:", font=("Helvica", 20))],
            *lista_pacientes,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        for chave, valor in values.items():
            if valor == True:
                dados = chave
                break
        self.close()
        if button is not None and button == "Confirmar":
            return dados
        else:
            return None

    def pegar_dados_agendar_atendimento(self, horario_atendimento: dict):
        sg.change_look_and_feel("LightGrey1")
        horas = [f"{h:02d}" for h in range(0, 24)]
        minutos = [f"{m:02d}" for m in range(0, 60, 1)]
        abre = horario_atendimento['abre']
        fecha = horario_atendimento['fecha']
        layout = [
            [sg.Text("DATA E HORA DO ATENDIMENTO", font=("Helvica", 25))],
            [sg.Text("Informe a data e o horário do atendimento:", font=("Helvica", 20))],
            [sg.Text(f"Horário de funcionamento da Clínica: {abre} às {fecha}", size=(50, 1))],
            [sg.Text("Data e hora do atendimento", size=(50, 1), font=("Helvica", 18))],
            [
                sg.Text("Data:", size=(7, 1)),
                sg.InputText("", key="data", size=(20, 1), readonly=True),
                sg.CalendarButton(
                    "Selecione a data",
                    target="data",
                    format="%Y-%m-%d",
                    close_when_date_chosen=True
                ),
                sg.Text("Horário Início:", size=(15, 1)),
                sg.Spin(horas, initial_value=abre.hour, key="hora_inicio", size=(3, 1), readonly=True),
                sg.Text(":"),
                sg.Spin(minutos, initial_value=abre.minute, key="minuto_inicio", size=(3, 1), readonly=True),
                sg.Text("Horário Fim:", size=(15, 1)),
                sg.Spin(horas, initial_value=abre.hour, key="hora_fim", size=(3, 1), readonly=True),
                sg.Text(":"),
                sg.Spin(minutos, initial_value=abre.minute, key="minuto_fim", size=(3, 1), readonly=True)
            ],
            [sg.Text("Valor da consulta (R$):", size=(24, 1)), sg.InputText("", key="valor")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        dados_bruto = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                dados = {
                    'data': Date.strptime(dados_bruto['data'], "%Y-%m-%d"),
                    'horario_inicio': Time(int(dados_bruto['hora_inicio']), int(dados_bruto['minuto_inicio'])),
                    'horario_fim': Time(int(dados_bruto['hora_fim']), int(dados_bruto['minuto_fim'])),
                    'valor': float(dados_bruto['valor'])
                }
                return dados
            except ValueError:
                sg.popup("Erro no valor do atendimento! Utilize ponto '.' para separar decimais.")
                return None
        else:
            return None

    def pegar_data_atendimento(self, datas: list):
        sg.change_look_and_feel("LightGrey1")
        lista_atendimentos = []
        for data in datas:
            lista_atendimentos.append([sg.Radio(f"{data}", "RD1", key=data)])

        layout = [
            [sg.Text("SELEÇÃO DE ATENDIMENTO", font=("Helvica", 25))],
            [sg.Text("Selecione a data do atendimento desejado:", font=("Helvica", 37))],
            *lista_atendimentos,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        for chave, valor in values.items():
            if valor == True:
                dados = chave
                break
        self.close()
        if button is not None and button == "Confirmar":
            return dados
        else:
            return None

    def pegar_horario_atendimento(self, horarios: list):
        sg.change_look_and_feel("LightGrey1")
        lista_atendimentos = []
        for horario in horarios:
            lista_atendimentos.append([sg.Radio(f"{horario}", "RD1", key=horario)])

        layout = [
            [sg.Text("SELEÇÃO DE ATENDIMENTO", font=("Helvica", 25))],
            [sg.Text("Selecione o horário do atendimento desejado:", font=("Helvica", 37))],
            *lista_atendimentos,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        for chave, valor in values.items():
            if valor == True:
                dados = chave
                break
        self.close()
        if button is not None and button == "Confirmar":
            return dados
        else:
            return None

    def pegar_procedimento(self, procedimentos: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_procedimentos = []
        for chave, valor in procedimentos.items():
            lista_procedimentos.append(
                [sg.Radio(f"Procedimento: {chave}, Responsável: {valor.profissional.nome}, Custo (R$): {valor.custo}",
                          "RD1", key=chave)]
            )

        layout = [
            [sg.Text("SELEÇÃO DE PROCEDIMENTO", font=("Helvica", 25))],
            [sg.Text("Selecione o procedimento desejado:", font=("Helvica", 37))],
            *lista_procedimentos,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        button, values = self.open()
        for chave, valor in values.items():
            if valor == True:
                dados = procedimentos[chave]
                break
        self.close()
        if button is not None and button == "Confirmar":
            return dados
        else:
            return None

    def mostrar_dados_da_consulta(self, dados: dict):
        sg.change_look_and_feel("LightGrey1")
        if len(dados["procedimentos_realizados"]) > 0:
            lista_procedimentos = [[sg.Text("Lista de Procedimentos", font=("Helvica", 14))]]
            for procedimento in dados["procedimentos_realizados"]:
                lista_procedimentos.append(
                    [sg.Text(
                        f"- {procedimento['descricao']},"
                        f" Custo: R$ {procedimento['custo']},"
                        f" Profissional: {procedimento['profissional']}",
                        font=("Helvica", 12))
                    ]
                )
        else:
            lista_procedimentos = []
        if dados["responsavel"] != None:
            responsavel = [sg.Text(f"Responsável: {dados['responsavel']}", font=("Helvica", 12))]
        else:
            responsavel = [sg.Text("", font=("Helvica", 12))]

        layout = [
            [sg.Text("CONSULTA ATENDIMENTOS", font=("Helvica", 25))],
            [sg.Text(f"Paciente: {dados['paciente']}", font=("Helvica", 12))],
            [sg.Text(f"Clínica: {dados['clinica']} - {dados['cidade']}", font=("Helvica", 12))],
            [sg.Text(f"Profissional: {dados['profissional']} - Especialidade: {dados['especialidade']}",
                     font=("Helvica", 12))],
            [sg.Text(f"Data: {dados['data']}, Horário: {dados['horario_inicio']} às {dados['horario_fim']}",
                     font=("Helvica", 12))],
            [sg.Text(f"Tipo de Atendimento: {dados['tipo_de_atendimento']}", font=("Helvica", 12))],
            [sg.Text(f"Valor: R$ {dados['valor']}", font=("Helvica", 12))],
            *lista_procedimentos,
            responsavel,
            [sg.Button("Fechar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        self.open()
        self.close()
        return None

    def mostrar_lista_atendimentos(self, dados: list):
        sg.change_look_and_feel("LightGrey1")
        lista_atendimentos = []
        for atendimento in dados:
            lista_atendimentos.append(
                f'Clínica: {atendimento["nome_clinica"]} [{atendimento["cnpj_clinica"]}]\n'
                f'Tipo: {atendimento["tipo_atendimento"]}\n'
                f'Data: {atendimento["data_atendimento"]} às {atendimento["hora_atendimento"]}\n'
                f'Profissional: {atendimento["nome_profissional"]}\n'
                f'Paciente: {atendimento["nome_paciente"]}\n'
                f'Valor: R$ {atendimento["valor_atendimento"]}\n'
                '-----------------------------------------------------\n\n'
            )
        listagem = "".join(lista_atendimentos)

        layout = [
            [sg.Text("LISTA DE ATENDIMENTOS", font=("Helvica", 25))],
            [sg.Multiline(default_text=listagem,
                          size=(70, 40),
                          disabled=True,
                          autoscroll=False)],
            [sg.Button("Fechar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

        self.open()
        self.close()
        return None
