import FreeSimpleGUI as sg


class ViewProfissionais():
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
            [sg.Text("MÓDULO DE GESTÃO DE PROFISSIONAIS", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Listar Profissionais", "RD1", key="1")],
            [sg.Radio("Cadastrar Profissional", "RD1", key="2")],
            [sg.Radio("Buscar Profissional", "RD1", key="3")],
            [sg.Radio("Excluir Profissional", "RD1", key="4")],
            [sg.Radio("Atualizar Nome do(a) Profissional", "RD1", key="5")],
            [sg.Radio("Atualizar Celular do(a) Profissional", "RD1", key="6")],
            [sg.Radio("Atualizar Especialidade do(a) Profissional", "RD1", key="7")],
            [sg.Radio("Atualizar Registro Profissional", "RD1", key="8")],
            [sg.Radio("Corrigir CPF do(a) Profissional", "RD1", key="9")],
            [sg.Radio("Retornar ao Menu Inicial", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

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

    def pegar_cpf(self, profissionais: dict):
        sg.change_look_and_feel("LightGrey1")
        lista_profissionais = []
        for cpf, valor in profissionais.items():
            lista_profissionais.append([sg.Radio(f"{valor.nome} [CPF: {cpf}]", "RD1", key=cpf)])

        layout = [
            [sg.Text("Selecione o(a) Profissional:", font=("Helvica", 20))],
            *lista_profissionais,
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

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

    def mostrar_dados_profissional(self, lista_dados: list):
        sg.change_look_and_feel("LightGrey1")
        if len(lista_dados) > 0:
            lista_profissionais = []
            for profissional in lista_dados:
                lista_profissionais.append(
                    f'Nome: {profissional["nome"]}\n'
                    f'Celular: {profissional["celular"]}\n'
                    f'CPF: {profissional["cpf"]}\n'
                    f'Especialidade: {profissional["especialidade"]}\n'
                    f'Registro Profissional: {profissional["registro_profissional"]}\n'
                    '--------------------------------------\n\n'
                )
            listagem = "".join(lista_profissionais)

            layout = [
                [sg.Text("PROFISSIONAL(IS) CADASTRADO(S)", font=("Helvica", 20))],
                [sg.Multiline(default_text=listagem,
                              size=(40, 40),
                              disabled=True,
                              autoscroll=False)],
                [sg.Button("Fechar")]
            ]
            self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

            self.open()
            self.close()
        else:
            sg.popup("Nenhum profissional encontrado!")

    def pegar_dados_profissional(self):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("CADASTRO DE PROFISSIONAL", font=("Helvica", 20))],
            [sg.Text("Dados do Profissional", font=("Helvica", 15))],
            [sg.Text("Nome", size=(20, 1)), sg.InputText("", key="nome")],
            [sg.Text("Celular", size=(20, 1)), sg.InputText("", key="celular")],
            [sg.Text("CPF", size=(20, 1)), sg.InputText("", key="cpf")],
            [sg.Text("Especialidade", size=(20, 1)), sg.InputText("", key="especialidade")],
            [sg.Text("Registro Profissional", size=(20, 1)),
             sg.InputText("", key="registro_profissional")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

        button, values = self.open()
        dados_bruto = values
        self.close()
        if button is not None and button == "Confirmar":
            dados = {
                'nome': dados_bruto['nome'],
                'celular': dados_bruto['celular'],
                'cpf': dados_bruto['cpf'],
                'especialidade': dados_bruto['especialidade'],
                'registro_profissional': dados_bruto['registro_profissional']
            }
            return dados
        else:
            return None

    def pegar_novo_nome(self, nome_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Nome do Profissional", font=("Helvica", 20))],
            [sg.Text(f"Nome anterior: {nome_anterior}", font=("Helvica", 15))],
            [sg.Text("Novo nome", size=(20, 1)), sg.InputText("", key="nome")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

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
            [sg.Text("Atualizar Celular do Profissional", font=("Helvica", 20))],
            [sg.Text(f"Celular anterior: {celular_anterior}", font=("Helvica", 15))],
            [sg.Text("Novo Celular", size=(20, 1)), sg.InputText("", key="novo_celular")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["novo_celular"]
        else:
            return None

    def pegar_nova_especialidade(self, especialidade_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Especialidade do Profissional", font=("Helvica", 20))],
            [sg.Text(f"Especialidade anterior: {especialidade_anterior}", font=("Helvica", 15))],
            [sg.Text("Nova especialidade", size=(20, 1)), sg.InputText("", key="nova_especialidade")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["nova_especialidade"]
        else:
            return None

    def pegar_novo_registro_profissional(self, registro_anterior: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Atualizar Registro Profissional", font=("Helvica", 20))],
            [sg.Text(f"Registro anterior: {registro_anterior}", font=("Helvica", 15))],
            [sg.Text("Novo registro", size=(20, 1)), sg.InputText("", key="novo_registro")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["novo_registro"]
        else:
            return None

    def pegar_cpf_correto(self, cpf_cadastrado: str):
        sg.change_look_and_feel("LightGrey1")
        layout = [
            [sg.Text("Corrigir CPF do(a) Profissional", font=("Helvica", 20))],
            [sg.Text(f"CPF cadastrado: {cpf_cadastrado}", font=("Helvica", 15))],
            [sg.Text("CPF correto", size=(20, 1)), sg.InputText("", key="cpf_correto")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        self.__window = sg.Window("Módulo de Gestão de Profissionais").layout(layout)

        button, values = self.open()
        dados = values
        self.close()
        if button is not None and button == "Confirmar":
            return dados["cpf_correto"]
        else:
            return None
