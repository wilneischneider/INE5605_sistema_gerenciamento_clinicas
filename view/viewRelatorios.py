import FreeSimpleGUI as sg


class ViewRelatorios():
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
            [sg.Text("MÓDULO DE EMISSÃO DE RELATÓRIOS", font=("Helvica", 20))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Clínicas com maior número de atendimentos", "RD1", key="1")],
            [sg.Radio("Atendimentos mais caros", "RD1", key="2")],
            [sg.Radio("Atendimentos mais baratos", "RD1", key="3")],
            [sg.Radio("Procedimentos mais realizados", "RD1", key="4")],
            [sg.Radio("Procedimentos mais caros", "RD1", key="5")],
            [sg.Radio("Procedimentos mais baratos", "RD1", key="6")],
            [sg.Radio("Retornar ao Menu Inicial", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Emissão de Relatórios").layout(layout)

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

    def mostrar_clinicas_com_mais_atendimentos(self, frequencia_atendimentos: dict, infos_clinicas: dict):
        sg.change_look_and_feel("LightGrey1")
        if len(frequencia_atendimentos) > 0:
            lista_clinicas = []
            for chave, valor in frequencia_atendimentos.items():
                lista_clinicas.append(f'Clínica: {infos_clinicas[chave]["nome"]} - {infos_clinicas[chave]["cidade"]}'
                                      f' [CNPJ: {chave}] -> Número de Atendimentos: {valor}\n\n')
            listagem = "".join(lista_clinicas)

            layout = [
                [sg.Text("10 CLÍNICAS COM MAIS ATENDIMENTOS", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(150, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Emissão de Relatórios").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum atendimento encontrado!")

    def mostrar_atendimentos_mais_caros(self, dados: list):
        sg.change_look_and_feel("LightGrey1")
        if len(dados) > 0:
            lista_atendimentos = []
            for atendimento in dados:
                lista_atendimentos.append(f'Clínica: {atendimento["nome_clinica"]} - {atendimento["cidade_clinica"]}'
                                          f' [CNPJ: {atendimento["cnpj_clinica"]}], Paciente:'
                                          f' {atendimento["nome_paciente"]}, Profissional:'
                                          f' {atendimento["nome_profissional"]}, Especialidade:'
                                          f' {atendimento["especialidade"]} -> Valor: R$ {atendimento["valor"]}\n\n')
            listagem = "".join(lista_atendimentos)

            layout = [
                [sg.Text("10 ATENDIMENTOS MAIS CAROS", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(200, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Emissão de Relatórios").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum atendimento encontrado!")

    def mostrar_atendimentos_mais_baratos(self, dados: list):
        sg.change_look_and_feel("LightGrey1")
        if len(dados) > 0:
            lista_atendimentos = []
            for atendimento in dados:
                lista_atendimentos.append(f'Clínica: {atendimento["nome_clinica"]} - {atendimento["cidade_clinica"]}'
                                          f' [CNPJ: {atendimento["cnpj_clinica"]}], Paciente:'
                                          f' {atendimento["nome_paciente"]}, Profissional:'
                                          f' {atendimento["nome_profissional"]}, Especialidade:'
                                          f' {atendimento["especialidade"]} -> Valor: R$ {atendimento["valor"]}\n\n')
            listagem = "".join(lista_atendimentos)

            layout = [
                [sg.Text("10 ATENDIMENTOS MAIS BARATOS", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(200, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Emissão de Relatórios").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum atendimento encontrado!")

    def mostrar_procedimentos_mais_realizados(self, dados: dict):
        sg.change_look_and_feel("LightGrey1")
        if len(dados) > 0:
            lista_procedimentos = []
            for chave, valor in dados.items():
                lista_procedimentos.append(f'Descrição: {chave}, Frequência: {valor}\n\n')
            listagem = "".join(lista_procedimentos)

            layout = [
                [sg.Text("10 PROCEDIMENTOS MAIS REALIZADOS", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(150, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Emissão de Relatórios").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum procedimento realizado!")

    def mostrar_procedimentos_mais_caros(self, dados: list):
        sg.change_look_and_feel("LightGrey1")
        if len(dados) > 0:
            lista_procedimentos = []
            for registro in dados:
                lista_procedimentos.append(f'Descrição: {registro["descricao"]}, Profissional:'
                                           f' {registro["nome_profissional"]}, Especialidade:'
                                           f' {registro["especialidade"]}, Valor: {registro["valor"]}\n\n')
            listagem = "".join(lista_procedimentos)

            layout = [
                [sg.Text("10 PROCEDIMENTOS MAIS CAROS", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(150, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Emissão de Relatórios").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum procedimento cadastrado!")

    def mostrar_procedimentos_mais_baratos(self, dados: list):
        sg.change_look_and_feel("LightGrey1")
        if len(dados) > 0:
            lista_procedimentos = []
            for registro in dados:
                lista_procedimentos.append(f'Descrição: {registro["descricao"]}, Profissional:'
                                           f' {registro["nome_profissional"]}, Especialidade:'
                                           f' {registro["especialidade"]}, Valor: {registro["valor"]}\n\n')
            listagem = "".join(lista_procedimentos)

            layout = [
                [sg.Text("10 PROCEDIMENTOS MAIS BARATOS", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(150, 25),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Emissão de Relatórios").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum procedimento cadastrado!")
