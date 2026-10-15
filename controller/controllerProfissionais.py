from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from model.pessoa import Pessoa
from model.profissional import Profissional
# from controller.controllerClinicas import ControllerClinica
from view.viewProfissionais import ViewProfissionais


class ControllerProfissional:
    def __init__(self, controller_sistema):
        self.__profissionais = {}
        self.__controller_sistema = controller_sistema
        self.__view_profissional = ViewProfissionais()

    @property
    def profissionais(self):
        return self.__profissionais

    def listar_profissionais_cadastrados(self):
        lista_dados = []
        for profissional in self.profissionais.values():
            registro = {"nome": profissional.nome, "cpf": profissional.cpf, "celular": profissional.celular,
                     "especialidade": profissional.especialidade,
                     "registro_profissional": profissional.registro_profissional}
            lista_dados.append(registro)
        self.__view_profissional.mostrar_dados_profissional(lista_dados)

    def listar_cpfs_cadastrados(self):
        return self.__profissionais.keys()

    def retornar_profissional(self):
        cpf = self.__view_profissional.pegar_cpf()
        if cpf in self.listar_cpfs_cadastrados():
            profissional = self.profissionais[cpf]
            lista_dados = [{"nome": profissional.nome, "cpf": profissional.cpf, "celular": profissional.celular,
                     "especialidade": profissional.especialidade,
                     "registro_profissional": profissional.registro_profissional}]
            self.__view_profissional.mostrar_dados_profissional(lista_dados)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{cpf}".')

    def cadastrar_profissional(self):
        dados = self.__view_profissional.pegar_dados_profissional()
        if dados["cpf"] not in self.listar_cpfs_cadastrados():
            try:
                profissional = Profissional(dados["nome"], dados["celular"], dados["cpf"],
                                            dados["especialidade"], dados["registro_profissional"])
                self.__profissionais.update({dados["cpf"]: profissional})
                self.__view_profissional.mostrar_mensagem('Profissional cadastrado(a) com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Profissional de CPF "{dados["cpf"]}" já cadastrado(a)!')

    def excluir_profissional(self):
        self.__view_profissional.mostrar_mensagem('--- Excluir Profissional ---')
        cpf = self.__view_profissional.pegar_cpf()
        if cpf in self.listar_cpfs_cadastrados():
            self.__profissionais.pop(cpf)
            self.__view_profissional.mostrar_mensagem(f'Profissional de CPF "{cpf}" excluído(a)!')
            # Excluir tambem o vinculo com as clinicas
            for cnpj in ControllerClinica.listar_cnpjs_cadastrados():
                msg = ControllerClinica.desvincular_profissional_das_clinicas(cnpj, cpf)
                self.__view_profissional.mostrar_mensagem(msg)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{cpf}".')

    def atualizar_nome(self):
        dados = self.__view_profissional.pegar_novo_nome()
        if dados["cpf"] in self.listar_cpfs_cadastrados():
            try:
                profissional = self.__profissionais[dados["cpf"]]
                profissional.nome = dados["nome"]
                self.__profissionais.update({dados["cpf"]:profissional})
                self.__view_profissional.mostrar_mensagem('Nome atualizado!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{dados["cpf"]}".')

    def atualizar_celular(self):
        dados = self.__view_profissional.pegar_novo_celular()
        if dados["cpf"] in self.listar_cpfs_cadastrados():
            try:
                profissional = self.__profissionais[dados["cpf"]]
                profissional.celular = dados["celular"]
                self.__profissionais.update({dados["cpf"]: profissional})
                self.__view_profissional.mostrar_mensagem('Celular atualizado!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{dados["cpf"]}".')

    def atualizar_especialidade(self):
        dados = self.__view_profissional.pegar_nova_especialidade()
        if dados["cpf"] in self.listar_cpfs_cadastrados():
            try:
                profissional = self.__profissionais[dados["cpf"]]
                profissional.especialidade = dados["especialidade"]
                self.__profissionais.update({dados["cpf"]: profissional})
                self.__view_profissional.mostrar_mensagem('Especialidade atualizada!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{dados["cpf"]}".')

    def atualizar_registro_profissional(self):
        dados = self.__view_profissional.pegar_novo_registro_profissional()
        if dados["cpf"] in self.listar_cpfs_cadastrados():
            try:
                profissional = self.__profissionais[dados["cpf"]]
                profissional.registro_profissional = dados["registro_profissional"]
                self.__profissionais.update({dados["cpf"]: profissional})
                self.__view_profissional.mostrar_mensagem('Registro profissional atualizado!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{dados["cpf"]}".')

    def corrigir_cpf(self):
        dados = self.__view_profissional.pegar_cpf_correto()
        if dados["cpf_correto"] not in self.listar_cpfs_cadastrados():
            if dados["cpf_cadastrado"] in self.listar_cpfs_cadastrados():
                try:
                    profissional = self.__profissionais[dados["cpf_cadastrado"]]
                    profissional.cpf = dados["cpf_correto"]
                    self.__profissionais.pop(dados["cpf_cadastrado"])
                    self.__profissionais.update({dados["cpf_correto"]: profissional})
                    self.__view_profissional.mostrar_mensagem("CPF corrigido com sucesso!")
                except TipoParametroIncorretoException as e:
                    self.__view_profissional.mostrar_mensagem(e)
            else:
                msg = f'Não há profissional cadastrado(a) com o CPF "{dados["cpf_cadastrado"]}".'
                self.__view_profissional.mostrar_mensagem(msg)
        else:
            msg = f'Já existe profissional com o CPF "{dados["cpf_correto"]}" cadastrado!'
            self.__view_profissional.mostrar_mensagem(msg)

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.listar_profissionais_cadastrados, 2: self.cadastrar_profissional,
                  3: self.retornar_profissional, 4: self.excluir_profissional, 5: self.atualizar_nome,
                  6: self.atualizar_celular, 7: self.atualizar_especialidade, 8: self.atualizar_registro_profissional,
                  9: self.corrigir_cpf}
        while True:
            opcoes[self.__view_profissional.view_opcoes()]()
