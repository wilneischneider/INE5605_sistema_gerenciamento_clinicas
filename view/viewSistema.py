import FreeSimpleGUI as sg


class ViewSistema():
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
            [sg.Text("SISTEMA DE GERENCIAMENTO DE CLÍNICAS", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Gerenciar Atendimentos", "RD1", key="1")],
            [sg.Radio("Gerenciar Pagamentos", "RD1", key="2")],
            [sg.Radio("Gerenciar Pacientes", "RD1", key="3")],
            [sg.Radio("Gerenciar Procedimentos", "RD1", key="4")],
            [sg.Radio("Gerenciar Profissionais", "RD1", key="5")],
            [sg.Radio("Gerenciar Clínicas", "RD1", key="6")],
            [sg.Radio("Gerenciar Tipos de Atendimento", "RD1", key="7")],
            [sg.Radio("Emitir Relatórios", "RD1", key="8")],
            [sg.Radio("Finalizar sistema", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Sistema de Gerenciamento de Clínicas").layout(layout)

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
