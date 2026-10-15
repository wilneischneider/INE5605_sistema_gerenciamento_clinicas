from model.paciente import Paciente
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from model.pessoa import Pessoa
from view.viewPacientes import ViewPacientes


class ControllerPaciente:
    def __init__(self, controller_sistema):
        self.__pacientes = {}
        self.__controller_sistema = controller_sistema
        self.__view_paciente = ViewPacientes()

    @property
    def pacientes(self):
        return self.__pacientes

    def listar_cpfs_cadastrados(self) -> list:
        return self.__pacientes.keys()

    def retornar_paciente(self):
        cpf = self.__view_paciente.pegar_cpf()
        if cpf in self.listar_cpfs_cadastrados():
            paciente = self.pacientes[cpf]
            lista_dados = [{"nome": paciente.nome, "celular": paciente.celular,
                     "cpf": paciente.cpf, "data_de_nascimento": paciente.data_de_nascimento}]
            self.__view_paciente.mostrar_dados_paciente(lista_dados)
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado com o CPF "{cpf}"!')

    def listar_pacientes(self):
        lista_dados = []
        for paciente in self.pacientes.values():
            registro = {"nome": paciente.nome, "celular": paciente.celular,
                     "cpf": paciente.cpf, "data_de_nascimento": paciente.data_de_nascimento}
            lista_dados.append(registro)
        self.__view_paciente.mostrar_dados_paciente(lista_dados)

    def cadastrar_paciente(self):
        dados = self.__view_paciente.pegar_dados_paciente()
        if dados["cpf"] not in self.listar_cpfs_cadastrados():
            try:
                paciente = Paciente(dados["nome"], dados["celular"], dados["cpf"], dados["data_de_nascimento"])
                self.__pacientes.update({dados["cpf"]: paciente})
                self.__view_paciente.mostrar_mensagem(f'Paciente cadastrado(a) com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_paciente.mostrar_mensagem(e)
        else:
            self.__view_paciente.mostrar_mensagem(f'Paciente de CPF "{dados["cpf"]}" já cadastrado!')

    def excluir_paciente(self):
        self.__view_paciente.mostrar_mensagem('--- Excluir Paciente ---')
        cpf = self.__view_paciente.pegar_cpf()
        if cpf in self.listar_cpfs_cadastrados():
            self.__pacientes.pop(cpf)
            self.__view_paciente.mostrar_mensagem(f'Paciente de CPF "{cpf}" excluído(a) com sucesso!')
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado(a) com o CPF "{cpf}"!')

    def atualizar_nome(self):
        dados = self.__view_paciente.pegar_novo_nome()
        if dados["cpf"] in self.listar_cpfs_cadastrados():
            try:
                paciente = self.__pacientes[dados["cpf"]]
                paciente.nome = dados["nome"]
                self.__pacientes.update({dados["cpf"]:paciente})
                self.__view_paciente.mostrar_mensagem('Nome atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_paciente.mostrar_mensagem(e)
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado(a) com o CPF "{dados["cpf"]}"!')

    def atualizar_celular(self):
        dados = self.__view_paciente.pegar_novo_celular()
        if dados["cpf"] in self.listar_cpfs_cadastrados():
            try:
                paciente = self.__pacientes[dados["cpf"]]
                paciente.celular = dados["celular"]
                self.__pacientes.update({dados["cpf"]: paciente})
                self.__view_paciente.mostrar_mensagem('Celular atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_paciente.mostrar_mensagem(e)
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado(a) com o CPF "{dados["cpf"]}"!')

    def corrigir_data_de_nascimento(self):
        dados = self.__view_paciente.pegar_data_de_nascimento()
        if dados["cpf"] in self.listar_cpfs_cadastrados():
            try:
                paciente = self.__pacientes[dados["cpf"]]
                paciente.data_de_nascimento = dados["data_de_nascimento"]
                self.__pacientes.update({dados["cpf"]: paciente})
                self.__view_paciente.mostrar_mensagem('Data de nascimento atualizada com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_paciente.mostrar_mensagem(e)
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado(a) com o CPF "{dados["cpf"]}"!')

    def corrigir_cpf(self):
        dados = self.__view_paciente.pegar_cpf_correto()
        if dados["cpf_correto"] not in self.listar_cpfs_cadastrados():
            if dados["cpf_cadastrado"] in self.listar_cpfs_cadastrados():
                try:
                    paciente = self.__pacientes[dados["cpf_cadastrado"]]
                    paciente.cpf = dados["cpf_correto"]
                    self.__pacientes.pop(dados["cpf_cadastrado"])
                    self.__pacientes.update({dados["cpf_correto"]: paciente})
                    self.__view_paciente.mostrar_mensagem("CPF corrigido com sucesso!")
                except TipoParametroIncorretoException as e:
                    self.__view_paciente.mostrar_mensagem(e)
            else:
                msg = f'Não há paciente cadastrado(a) com o CPF "{dados["cpf_cadastrado"]}".'
                self.__view_paciente.mostrar_mensagem(msg)
        else:
            msg = f'Já existe paciente com o CPF "{dados["cpf_correto"]}" cadastrado!'
            self.__view_paciente.mostrar_mensagem(msg)

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.cadastrar_paciente, 2: self.retornar_paciente, 3: self.listar_pacientes,
                  4: self.excluir_paciente, 5: self.atualizar_nome, 6: self.atualizar_celular,
                  7: self.corrigir_data_de_nascimento, 8: self.corrigir_cpf}
        while True:
            opcoes[self.__view_paciente.view_opcoes()]()
