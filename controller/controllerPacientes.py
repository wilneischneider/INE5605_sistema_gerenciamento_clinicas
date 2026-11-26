from model.paciente import Paciente
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from view.viewPacientes import ViewPacientes
from daos.daoPacientes import DaoPacientes


class ControllerPaciente:
    def __init__(self, controller_sistema):
        self.__pacientes_dao = DaoPacientes()
        self.__controller_sistema = controller_sistema
        self.__view_paciente = ViewPacientes()

    def pacientes(self):
        return self.__pacientes_dao.get_dict()

    def listar_cpfs_cadastrados(self) -> list:
        pacientes = self.pacientes()
        return list(pacientes.keys())

    def retornar_paciente(self):
        pacientes = self.pacientes()
        if len(pacientes) == 0:
            self.__view_paciente.mostrar_mensagem('Nenhum paciente cadastrado!')
            self.abrir_tela()
        cpf = self.__view_paciente.pegar_cpf(pacientes)
        if cpf == None:
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            paciente = pacientes[cpf]
            lista_dados = [{"nome": paciente.nome, "celular": paciente.celular,
                     "cpf": paciente.cpf, "data_de_nascimento": paciente.data_de_nascimento}]
            self.__view_paciente.mostrar_dados_paciente(lista_dados)
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado com o CPF "{cpf}"!')

    def listar_pacientes(self):
        lista_dados = []
        pacientes = self.pacientes()
        for paciente in pacientes.values():
            registro = {"nome": paciente.nome, "celular": paciente.celular,
                     "cpf": paciente.cpf, "data_de_nascimento": paciente.data_de_nascimento}
            lista_dados.append(registro)
        self.__view_paciente.mostrar_dados_paciente(lista_dados)
        self.abrir_tela()

    def cadastrar_paciente(self):
        dados = self.__view_paciente.pegar_dados_paciente()
        if dados == None:
            self.abrir_tela()
        if (
            len(dados["nome"]) == 0
            or len(dados["celular"]) == 0
            or len(dados["cpf"]) == 0
            or dados["data_de_nascimento"] == None
        ):
            self.__view_paciente.mostrar_mensagem('Todos os campos devem ser preenchidos!')
            self.abrir_tela()
        if dados["cpf"] not in self.listar_cpfs_cadastrados():
            try:
                paciente = Paciente(dados["nome"], dados["celular"], dados["cpf"], dados["data_de_nascimento"])
                self.__pacientes_dao.add(paciente)
                self.__view_paciente.mostrar_mensagem(f'Paciente cadastrado(a) com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_paciente.mostrar_mensagem(e)
        else:
            self.__view_paciente.mostrar_mensagem(f'Paciente de CPF "{dados["cpf"]}" já cadastrado!')

    def excluir_paciente(self):
        pacientes = self.pacientes()
        if len(pacientes) == 0:
            self.__view_paciente.mostrar_mensagem('Nenhum paciente cadastrado!')
            self.abrir_tela()
        cpf = self.__view_paciente.pegar_cpf(pacientes)
        if cpf == None:
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            self.__pacientes_dao.remove(cpf)
            self.__view_paciente.mostrar_mensagem(f'Paciente de CPF "{cpf}" excluído(a) com sucesso!')
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado(a) com o CPF "{cpf}"!')

    def atualizar_nome(self):
        pacientes = self.pacientes()
        if len(pacientes) == 0:
            self.__view_paciente.mostrar_mensagem('Nenhum paciente cadastrado!')
            self.abrir_tela()
        cpf = self.__view_paciente.pegar_cpf(pacientes)
        if cpf == None:
            self.abrir_tela()
        paciente = pacientes[cpf]
        nome_anterior = paciente.nome
        novo_nome = self.__view_paciente.pegar_novo_nome(nome_anterior)
        if novo_nome == None:
            self.abrir_tela()
        if len(novo_nome) == 0:
            self.__view_paciente.mostrar_mensagem('Obrigatório preencher Nome!')
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            try:
                paciente.nome = novo_nome
                self.__pacientes_dao.update(paciente)
                self.__view_paciente.mostrar_mensagem('Nome atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_paciente.mostrar_mensagem(e)
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado(a) com o CPF "{dados["cpf"]}"!')

    def atualizar_celular(self):
        pacientes = self.pacientes()
        if len(pacientes) == 0:
            self.__view_paciente.mostrar_mensagem('Nenhum paciente cadastrado!')
            self.abrir_tela()
        cpf = self.__view_paciente.pegar_cpf(pacientes)
        if cpf == None:
            self.abrir_tela()
        paciente = pacientes[cpf]
        celular_anterior = paciente.celular
        novo_celular = self.__view_paciente.pegar_novo_celular(celular_anterior)
        if novo_celular == None:
            self.abrir_tela()
        if len(novo_celular) == 0:
            self.__view_paciente.mostrar_mensagem('Obrigatório preencher Celular!')
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            try:
                paciente.celular = novo_celular
                self.__pacientes_dao.update(paciente)
                self.__view_paciente.mostrar_mensagem('Celular atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_paciente.mostrar_mensagem(e)
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado(a) com o CPF "{dados["cpf"]}"!')

    def corrigir_data_de_nascimento(self):
        pacientes = self.pacientes()
        if len(pacientes) == 0:
            self.__view_paciente.mostrar_mensagem('Nenhum paciente cadastrado!')
            self.abrir_tela()
        cpf = self.__view_paciente.pegar_cpf(pacientes)
        if cpf == None:
            self.abrir_tela()
        paciente = pacientes[cpf]
        data_nascimento_anterior = paciente.data_de_nascimento
        nova_data_nascimento = self.__view_paciente.pegar_data_de_nascimento(data_nascimento_anterior)
        if nova_data_nascimento == None:
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            try:
                paciente.data_de_nascimento = nova_data_nascimento
                self.__pacientes_dao.update(paciente)
                self.__view_paciente.mostrar_mensagem('Data de nascimento atualizada com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_paciente.mostrar_mensagem(e)
        else:
            self.__view_paciente.mostrar_mensagem(f'Não há paciente cadastrado(a) com o CPF "{dados["cpf"]}"!')

    def corrigir_cpf(self):
        pacientes = self.pacientes()
        if len(pacientes) == 0:
            self.__view_paciente.mostrar_mensagem('Nenhum paciente cadastrado!')
            self.abrir_tela()
        cpf = self.__view_paciente.pegar_cpf(pacientes)
        if cpf == None:
            self.abrir_tela()
        paciente = pacientes[cpf]
        cpf_cadastrado = paciente.cpf
        cpf_correto = self.__view_paciente.pegar_cpf_correto(cpf_cadastrado)
        if cpf_correto == None:
            self.abrir_tela()
        if len(cpf_correto) == 0:
            self.__view_paciente.mostrar_mensagem('Obrigatório preencher CPF!')
            self.abrir_tela()
        if cpf_correto not in self.listar_cpfs_cadastrados():
            if cpf_cadastrado in self.listar_cpfs_cadastrados():
                try:
                    paciente.cpf = cpf_correto
                    self.__pacientes_dao.remove(cpf_cadastrado)
                    self.__pacientes_dao.add(paciente)
                    self.__view_paciente.mostrar_mensagem("CPF corrigido com sucesso!")
                except TipoParametroIncorretoException as e:
                    self.__view_paciente.mostrar_mensagem(e)
            else:
                msg = f'Não há paciente cadastrado(a) com o CPF "{cpf_cadastrado}".'
                self.__view_paciente.mostrar_mensagem(msg)
        else:
            msg = f'Já existe paciente com o CPF "{cpf_correto}" cadastrado!'
            self.__view_paciente.mostrar_mensagem(msg)

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.cadastrar_paciente, 2: self.retornar_paciente, 3: self.listar_pacientes,
                  4: self.excluir_paciente, 5: self.atualizar_nome, 6: self.atualizar_celular,
                  7: self.corrigir_data_de_nascimento, 8: self.corrigir_cpf}
        while True:
            opcoes[self.__view_paciente.view_opcoes()]()
