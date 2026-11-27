import FreeSimpleGUI as sg


class ViewTiposDeAtendimento():
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
            [sg.Text("MÓDULO DE GESTÃO DE TIPOS DE ATENDIMENTO", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Listar Tipos de Atendimento", "RD1", key="1")],
            [sg.Radio("Cadastrar Tipo de Atendimento", "RD1", key="2")],
            [sg.Radio("Excluir Tipo de Atendimento", "RD1", key="3")],
            [sg.Radio("Retornar ao Menu Inicial", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Atendimentos").layout(layout)

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

    def mostrar_tipos_atendimento(self, tipos: list):
        sg.change_look_and_feel("LightGrey1")
        if len(tipos) > 0:
            lista_tipos = []
            for tipo in tipos:
                lista_tipos.append(
                    f'Tipo: {tipo}\n'
                    '--------------------------------------\n\n'
                )
            listagem = "".join(lista_tipos)

            layout = [
                [sg.Text("TIPOS DE ATENDIMENTO CADASTRADOS", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(40, 40),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Tipos de Atendimento").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum tipo de atendimento cadastrado!")

    def pegar_tipo_atendimento(self, tipos: list):
        sg.change_look_and_feel("LightGrey1")
        lista_tipos_atendimento = []
        for tipo in tipos:
            lista_tipos_atendimento.append([sg.Radio(f"{tipo}", "RD1", key=tipo)])

        layout = [
            [sg.Text("Exclusão de Tipo de Atendimento", font=("Helvica", 20))],
            [sg.Text("Selecione o tipo de atendimento desejado:", font=("Helvica", 15))],
            *lista_tipos_atendimento,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Tipos de Atendimento").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            for tipo, resposta in dados.items():
                if resposta == True:
                    return tipo
                    break
        else:
            return None

    def pegar_dados_tipo_atendimento(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("CADASTRO DE TIPO DE ATENDIMENTO", font=("Helvica", 20))],
            [sg.Text("Dados do Tipo de Atendimento", font=("Helvica", 15))],
            [sg.Text("Tipo", size=(20, 1)), sg.InputText("", key="tipo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Tipos de Atendimento").layout(layout)

        button, values = self.open()
        dados_bruto = values
        self.close()
        if button is not None and button == "Confirmar":
            dados = dados_bruto["tipo"]
            return dados
        else:
            return None
