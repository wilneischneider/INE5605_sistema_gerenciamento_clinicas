import FreeSimpleGUI as sg
from datetime import time as Time


class ViewClinicas():
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
            [sg.Text("MÓDULO DE GESTÃO DE CLÍNICAS", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Listar Clínicas", "RD1", key="1")],
            [sg.Radio("Cadastrar Clínica", "RD1", key="2")],
            [sg.Radio("Buscar Clínica", "RD1", key="3")],
            [sg.Radio("Excluir Clínica", "RD1", key="4")],
            [sg.Radio("Atualizar Nome de Clínica", "RD1", key="5")],
            [sg.Radio("Atualizar Cidade de Clínica", "RD1", key="6")],
            [sg.Radio("Atualizar Descrição de Clínica", "RD1", key="7")],
            [sg.Radio("Corrigir CNPJ de Clínica", "RD1", key="8")],
            [sg.Radio("Atualizar Horário de Abertura de Clínica", "RD1", key="9")],
            [sg.Radio("Atualizar Horário de Fechamento de Clínica", "RD1", key="10")],
            [sg.Radio("Listar Profissionais de Clínica", "RD1", key="11")],
            [sg.Radio("Vincular Profissional à Clínica", "RD1", key="12")],
            [sg.Radio("Desvincular Profissional de Clínica", "RD1", key="13")],
            [sg.Radio("Retornar ao Menu Inicial", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

    def view_opcoes(self):
        self.init_opcoes()
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

    def mostrar_clinicas(self, clinicas: list):
        sg.change_look_and_feel("LightGrey1")
        lista_clinicas = []
        for clinica in clinicas:
            lista_clinicas.append(
                f'Nome: {clinica.nome}\n'
                f'CNPJ: {clinica.cnpj}\n'
                f'Cidade: {clinica.cidade}\n'
                f'Descrição: {clinica.descricao}\n'
                f'Horário de funcionamento: {clinica.horario_de_abertura} às {clinica.horario_de_fechamento}\n'
                '-----------------------------------------------------\n\n'
            )
        listagem = "".join(lista_clinicas)

        layout = [
            [sg.Text("LISTA DE CLÍNICAS", font=("Helvica", 25))],
            [sg.Multiline(default_text=listagem,
                          size=(70, 40),
                          disabled=True,
                          autoscroll=False)],
            [sg.Button("Fechar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

        self.open()
        self.close()
        return None

    def pegar_dados_da_clinica(self):
        sg.change_look_and_feel("LightGrey1")
        horas = [f"{h:02d}" for h in range(0, 24)]
        minutos = [f"{m:02d}" for m in range(0, 60, 1)]
        layout = [
            [sg.Text("CADASTRAR CLÍNICA", font=("Helvica", 25))],
            [sg.Text("Informe os dados da clínica", font=("Helvica", 15))],
            [sg.Text("Nome", size=(20, 1)), sg.InputText("", key="nome")],
            [sg.Text("CNPJ", size=(20, 1)), sg.InputText("", key="cnpj")],
            [sg.Text("Cidade", size=(20, 1)), sg.InputText("", key="cidade")],
            [sg.Text("Descrição", size=(20, 1)), sg.InputText("", key="descricao")],
            [
                sg.Text("Horário de abertura:", size=(20, 1)),
                sg.Spin(horas, initial_value="00", key="hora_inicio", size=(3, 1), readonly=True),
                sg.Text(":"),
                sg.Spin(minutos, initial_value="00", key="minuto_inicio", size=(3, 1), readonly=True),
                sg.Text("Horário de fechamento:", size=(20, 1)),
                sg.Spin(horas, initial_value="00", key="hora_fim", size=(3, 1), readonly=True),
                sg.Text(":"),
                sg.Spin(minutos, initial_value="00", key="minuto_fim", size=(3, 1), readonly=True)
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

        button, values = self.open()
        dados_bruto = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                dados = {
                    "nome": dados_bruto["nome"],
                    "cnpj": dados_bruto["cnpj"],
                    "cidade": dados_bruto["cidade"],
                    "descricao": dados_bruto["descricao"],
                    "horario_de_abertura": Time(int(dados_bruto['hora_inicio']), int(dados_bruto['minuto_inicio'])),
                    "horario_de_fechamento": Time(int(dados_bruto['hora_fim']), int(dados_bruto['minuto_fim']))
                }
                return dados
            except ValueError:
                sg.popup("Erro nos horários informados!")
                return None
        else:
            return None

    def pegar_cnpj(self, clinicas: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_clinicas = []
        for cnpj, valor in clinicas.items():
            lista_clinicas.append(
                [sg.Radio(f"{valor.nome} - {valor.cidade} [CNPJ: {cnpj}]",
                          "RD1", key=cnpj)]
            )

        layout = [
            [sg.Text("SELEÇÃO DE CLÍNICA", font=("Helvica", 25))],
            [sg.Text("Selecione a clínica desejada:", font=("Helvica", 37))],
            *lista_clinicas,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

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

    def pegar_novo_nome(self, nome_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Nome da Clínica", font=("Helvica", 20))],
            [sg.Text(f"Nome anterior: {nome_anterior}", font=("Helvica", 15))],
            [sg.Text("Novo nome", size=(20, 1)), sg.InputText("", key="nome")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["nome"]
        else:
            return None

    def pegar_nova_cidade(self, cidade_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Cidade da Clínica", font=("Helvica", 20))],
            [sg.Text(f"Cidade anterior: {cidade_anterior}", font=("Helvica", 15))],
            [sg.Text("Nova cidade", size=(20, 1)), sg.InputText("", key="cidade")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["cidade"]
        else:
            return None

    def pegar_nova_descricao(self, descricao_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Descrição da Clínica", font=("Helvica", 20))],
            [sg.Text(f"Descrição anterior: {descricao_anterior}", font=("Helvica", 15))],
            [sg.Text("Nova descrição", size=(20, 1)), sg.InputText("", key="descricao")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["descricao"]
        else:
            return None

    def pegar_cnpj_correto(self, cnpj_cadastrado: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Corrigir CNPJ da Clínica", font=("Helvica", 20))],
            [sg.Text(f"CNPJ cadastrado: {cnpj_cadastrado}", font=("Helvica", 15))],
            [sg.Text("CNPJ correto", size=(20, 1)), sg.InputText("", key="cnpj")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["cnpj"]
        else:
            return None

    def pegar_novo_horario_de_abertura(self, horario_anterior: Time):
        sg.change_look_and_feel("LightGrey1")
        horas = [f"{h:02d}" for h in range(0, 24)]
        minutos = [f"{m:02d}" for m in range(0, 60, 1)]
        layout = [
            [sg.Text("Atualizar Horário de Abertura da Clínica", font=("Helvica", 20))],
            [sg.Text(f"Horário anterior: {horario_anterior}", font=("Helvica", 15))],
            [
                sg.Text("Novo horário de abertura:", size=(20, 1)),
                sg.Spin(horas, initial_value="00", key="hora_inicio", size=(3, 1), readonly=True),
                sg.Text(":"),
                sg.Spin(minutos, initial_value="00", key="minuto_inicio", size=(3, 1), readonly=True)
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                novo_horario_abertura = Time(int(dados['hora_inicio']), int(dados['minuto_inicio']))
                return novo_horario_abertura
            except ValueError:
                sg.popup("Erro nos horários informados!")
                return None
        else:
            return None

    def pegar_novo_horario_de_fechamento(self, horario_anterior: Time):
        sg.change_look_and_feel("LightGrey1")
        horas = [f"{h:02d}" for h in range(0, 24)]
        minutos = [f"{m:02d}" for m in range(0, 60, 1)]
        layout = [
            [sg.Text("Atualizar Horário de Fechamento da Clínica", font=("Helvica", 20))],
            [sg.Text(f"Horário anterior: {horario_anterior}", font=("Helvica", 15))],
            [
                sg.Text("Novo horário de fechamento:", size=(20, 1)),
                sg.Spin(horas, initial_value="00", key="hora_fim", size=(3, 1), readonly=True),
                sg.Text(":"),
                sg.Spin(minutos, initial_value="00", key="minuto_fim", size=(3, 1), readonly=True)
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                novo_horario_fechamento = Time(int(dados['hora_fim']), int(dados['minuto_fim']))
                return novo_horario_fechamento
            except ValueError:
                sg.popup("Erro nos horários informados!")
                return None
        else:
            return None

    def pegar_cpf_vincular_desvincular(self, profissionais: dict):
        sg.change_look_and_feel("LightGrey1")
        if len(profissionais) == 0:
            sg.popup("Nenhum profissional encontrado!")
            return None
        else:
            lista_profissionais = []
            for cpf, valor in profissionais.items():
                lista_profissionais.append(
                    [sg.Radio(f"{valor.nome} [CPF: {cpf}]", "RD1", key=cpf)]
                )

            layout = [
                [sg.Text("SELEÇÃO DE PROFISSIONAL", font=("Helvica", 25))],
                [sg.Text("Selecione o(a) profissional desejado(a):", font=("Helvica", 37))],
                *lista_profissionais,
                [sg.Button("Confirmar"), sg.Button("Cancelar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

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

    def mostrar_profissionais(self, lista_dados: list):
        sg.change_look_and_feel("LightGrey1")
        if len(lista_dados) > 0:
            lista_profissionais = []
            for profissional in lista_dados:
                lista_profissionais.append(
                    f'Nome: {profissional["nome"]}\n'
                    f'CPF: {profissional["cpf"]}\n'
                    f'Celular: {profissional["celular"]}\n'
                    f'Especialidade: {profissional["especialidade"]}\n'
                    '--------------------------------------\n\n'
                )
            listagem = "".join(lista_profissionais)

            layout = [
                [sg.Text("PROFISSIONAL(IS) VINCULADO(S) À CLÍNICA", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(40, 40),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Clínicas").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum profissional encontrado!")
