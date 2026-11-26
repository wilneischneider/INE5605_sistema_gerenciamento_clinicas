import FreeSimpleGUI as sg


class ViewProcedimentos():
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
            [sg.Text("MÓDULO DE GESTÃO DE PROCEDIMENTOS", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Cadastrar Procedimento", "RD1", key="1")],
            [sg.Radio("Buscar Procedimento", "RD1", key="2")],
            [sg.Radio("Listar Procedimentos", "RD1", key="3")],
            [sg.Radio("Excluir Procedimento", "RD1", key="4")],
            [sg.Radio("Alterar Custo do Procedimento", "RD1", key="5")],
            [sg.Radio("Alterar Profissional Responsável", "RD1", key="6")],
            [sg.Radio("Corrigir Descrição", "RD1", key="7")],
            [sg.Radio("Retornar ao Menu Inicial", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Procedimentos").layout(layout)

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
        if values["0"] or button in (None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)

    def pegar_descricao(self, descricoes: list):
        sg.change_look_and_feel("LightGrey1")
        lista_descricoes = []
        for descricao in descricoes:
            lista_descricoes.append([sg.Radio(f"{descricao}", "RD1", key=descricao)])

        layout = [
            [sg.Text("Selecione o procedimento desejado:", font=("Helvica", 20))],
            *lista_descricoes,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Procedimentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            for descricao, resposta in dados.items():
                if resposta == True:
                    return descricao
                    break
        else:
            return None

    def mostrar_dados_procedimento(self, lista_dados:list):
        sg.change_look_and_feel("LightGrey1")
        if len(lista_dados) > 0:
            lista_procedimentos = []
            for procedimento in lista_dados:
                lista_procedimentos.append(
                    f'Descrição: {procedimento["descricao"]}\n'
                    f'Custo: {procedimento["custo"]}\n'
                    f'Profissional responsável: {procedimento["profissional"]}\n'
                    '--------------------------------------\n\n'
                )
            listagem = "".join(lista_procedimentos)

            layout = [
                [sg.Text("PROCEDIMENTO(S) CADASTRADO(S)", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(40, 40),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Procedimentos").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum procedimento encontrado!")

    def pegar_dados_procedimento(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("CADASTRO DE PROCEDIMENTO", font=("Helvica", 20))],
            [sg.Text("Dados do Procedimento", font=("Helvica", 15))],
            [sg.Text("Descrição", size=(20, 1)), sg.InputText("", key="descricao")],
            [sg.Text("Custo", size=(20, 1)), sg.InputText("", key="custo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Procedimentos").layout(layout)

        button, values = self.open()
        dados_bruto = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                dados = {
                    "descricao": dados_bruto["descricao"],
                    "custo": float(dados_bruto["custo"])
                }
                return dados
            except ValueError:
                sg.popup("No custo, informe apenas valores e utilize ponto '.' como separador de decimal.")
                return None
        else:
            return None

    def pegar_cpf(self, profissionais: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_profissionais = []
        for cpf, valor in profissionais.items():
            lista_profissionais.append([sg.Radio(f"{valor.nome} [CPF: {cpf}]", "RD1", key=cpf)])

        layout = [
            [sg.Text("Selecione o(a) Profissional Responsável:", font=("Helvica", 20))],
            *lista_profissionais,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Procedimentos").layout(layout)

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

    def pegar_novo_custo(self, custo_anterior: float):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Custo do Procedimento", font=("Helvica", 20))],
            [sg.Text(f"Custo anterior: R$ {custo_anterior}", font=("Helvica", 15))],
            [sg.Text("Novo custo (R$)", size=(20, 1)), sg.InputText("", key="novo_custo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Procedimentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            try:
                novo_custo = float(dados["novo_custo"])
                return novo_custo
            except ValueError:
                sg.popup("No custo, informe apenas valores e utilize ponto '.' como separador de decimal.")
                return None
        else:
            return None

    def pegar_novo_profissional(self, profissional_anterior: str, profissionais: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_profissionais = []
        for cpf, valor in profissionais.items():
            lista_profissionais.append([sg.Radio(f"{valor.nome} [CPF: {cpf}]", "RD1", key=cpf)])

        layout = [
            [sg.Text("Atualizar Profissional Responsável", font=("Helvica", 20))],
            [sg.Text(f"Profissional anterior: {profissional_anterior}", font=("Helvica", 15))],
            [sg.Text("Selecione o(a) Novo(a) Profissional Responsável:", font=("Helvica", 12))],
            *lista_profissionais,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Procedimentos").layout(layout)

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

    def pegar_descricao_correta(self, descricao_cadastrada: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Descrição do Procedimento", font=("Helvica", 20))],
            [sg.Text(f"Descrição cadastrada: {descricao_cadastrada}", font=("Helvica", 15))],
            [sg.Text("Nova descrição", size=(20, 1)), sg.InputText("", key="nova_descricao")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Procedimentos").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["nova_descricao"]
        else:
            return None
