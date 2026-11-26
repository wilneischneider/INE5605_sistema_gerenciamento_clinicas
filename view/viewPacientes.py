from datetime import date as Date
import FreeSimpleGUI as sg


class ViewPacientes():
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
            [sg.Text("MÓDULO DE GESTÃO DE PACIENTES", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Cadastrar Paciente", "RD1", key="1")],
            [sg.Radio("Buscar Paciente", "RD1", key="2")],
            [sg.Radio("Listar Pacientes", "RD1", key="3")],
            [sg.Radio("Excluir Paciente", "RD1", key="4")],
            [sg.Radio("Atualizar Nome do(a) Paciente", "RD1", key="5")],
            [sg.Radio("Atualizar Celular do(a) Paciente", "RD1", key="6")],
            [sg.Radio("Corrigir Data de Nascimento do(a) Paciente", "RD1", key="7")],
            [sg.Radio("Corrigir CPF do(a) Paciente", "RD1", key="8")],
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
        if values["6"]:
            opcao = 6
        if values["7"]:
            opcao = 7
        if values["8"]:
            opcao = 8
        if values["0"] or button in (None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao

    def pegar_dados_paciente(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("CADASTRO DE PACIENTE", font=("Helvica", 20))],
            [sg.Text("Dados do Paciente", font=("Helvica", 15))],
            [sg.Text("Nome", size=(20, 1)), sg.InputText("", key="nome")],
            [sg.Text("Celular", size=(20, 1)), sg.InputText("", key="celular")],
            [sg.Text("CPF", size=(20, 1)), sg.InputText("", key="cpf")],
            [
                sg.Text("Data de Nascimento:", size=(20, 1)),
                sg.InputText("", key="data", size=(20, 1), readonly=True),
                sg.CalendarButton(
                    "Selecione a data",
                    target="data",
                    format="%Y-%m-%d",
                    close_when_date_chosen=True
                )
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pacientes").layout(layout)

        button, values = self.open()
        dados_bruto = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                dados = {
                    'nome': dados_bruto['nome'],
                    'celular': dados_bruto['celular'],
                    'cpf': dados_bruto['cpf'],
                    'data_de_nascimento': Date.strptime(dados_bruto['data'], "%Y-%m-%d")
                }
                return dados
            except ValueError:
                sg.popup("Obrigatório selecionar a data de nascimento!")
        else:
            return None

    def mostrar_dados_paciente(self, lista_dados:list):
        sg.change_look_and_feel("LightGrey1")
        if len(lista_dados) > 0:
            lista_pacientes = []
            for paciente in lista_dados:
                lista_pacientes.append(
                    f'Nome: {paciente["nome"]}\n'
                    f'Celular: {paciente["celular"]}\n'
                    f'CPF: {paciente["cpf"]}\n'
                    f'Data de Nascimento: {paciente["data_de_nascimento"]}\n'
                    '--------------------------------------\n\n'
                )
            listagem = "".join(lista_pacientes)

            layout = [
                [sg.Text("PACIENTE(S) CADASTRADO(S)", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(40, 40),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Pacientes").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum paciente encontrado!")

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def pegar_cpf(self, pacientes: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_pacientes = []
        for cpf, valor in pacientes.items():
            lista_pacientes.append([sg.Radio(f"{valor.nome} [CPF: {cpf}]", "RD1", key=cpf)])

        layout = [
            [sg.Text("Selecione o(a) Paciente:", font=("Helvica", 20))],
            *lista_pacientes,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pacientes").layout(layout)

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

    def pegar_novo_nome(self, nome_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Nome do Paciente", font=("Helvica", 20))],
            [sg.Text(f"Nome anterior: {nome_anterior}", font=("Helvica", 15))],
            [sg.Text("Novo nome", size=(20, 1)), sg.InputText("", key="nome")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pacientes").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["nome"]
        else:
            return None

    def pegar_novo_celular(self, celular_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Celular do Paciente", font=("Helvica", 20))],
            [sg.Text(f"Celular anterior: {celular_anterior}", font=("Helvica", 15))],
            [sg.Text("Novo celular", size=(20, 1)), sg.InputText("", key="celular")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pacientes").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["celular"]
        else:
            return None

    def pegar_data_de_nascimento(self, data_de_nascimento_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Corrigir data de nascimento do Paciente", font=("Helvica", 20))],
            [sg.Text(f"Data anterior: {data_de_nascimento_anterior}", font=("Helvica", 15))],
            [
                sg.Text("Data correta:", size=(20, 1)),
                sg.InputText("", key="data_de_nascimento", size=(20, 1), readonly=True),
                sg.CalendarButton(
                    "Selecione a data",
                    target="data_de_nascimento",
                    format="%Y-%m-%d",
                    close_when_date_chosen=True
                )
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pacientes").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                return Date.strptime(dados['data_de_nascimento'], "%Y-%m-%d")
            except ValueError:
                sg.popup("Obrigatório preencher Data de Nascimento!")
                return None
        else:
            return None

    def pegar_cpf_correto(self, cpf_cadastrado: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Corrigir CPF do Paciente", font=("Helvica", 20))],
            [sg.Text(f"CPF cadastrado: {cpf_cadastrado}", font=("Helvica", 15))],
            [sg.Text("CPF correto", size=(20, 1)), sg.InputText("", key="cpf_correto")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Pacientes").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["cpf_correto"]
        else:
            return None
