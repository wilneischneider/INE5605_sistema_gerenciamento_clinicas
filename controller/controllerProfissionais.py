from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from model.pessoa import Pessoa
from model.profissional import Profissional
from view.viewProfissionais import ViewProfissionais
from daos.daoProfissionais import DaoProfissionais


class ControllerProfissional:
    def __init__(self, controller_sistema):
        self.__profissionais_dao = DaoProfissionais()
        self.__controller_sistema = controller_sistema
        self.__view_profissional = ViewProfissionais()

    def profissionais(self):
        return self.__profissionais_dao.get_dict()

    def listar_profissionais_cadastrados(self):
        lista_dados = []
        for profissional in self.__profissionais_dao.get_all():
            registro = {"nome": profissional.nome, "cpf": profissional.cpf, "celular": profissional.celular,
                     "especialidade": profissional.especialidade,
                     "registro_profissional": profissional.registro_profissional}
            lista_dados.append(registro)
        self.__view_profissional.mostrar_dados_profissional(lista_dados)

    def listar_cpfs_cadastrados(self):
        profissionais = self.profissionais()
        return list(profissionais.keys())

    def retornar_profissional(self):
        profissionais = self.profissionais()
        if len(profissionais) == 0:
            self.__view_profissional.mostrar_mensagem('Nenhum profissional cadastrado!')
            self.abrir_tela()
        cpf = self.__view_profissional.pegar_cpf(profissionais)
        if cpf == None:
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            profissional = profissionais[cpf]
            lista_dados = [{"nome": profissional.nome, "cpf": profissional.cpf, "celular": profissional.celular,
                     "especialidade": profissional.especialidade,
                     "registro_profissional": profissional.registro_profissional}]
            self.__view_profissional.mostrar_dados_profissional(lista_dados)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{cpf}".')

    def cadastrar_profissional(self):
        dados = self.__view_profissional.pegar_dados_profissional()
        if dados == None:
            self.abrir_tela()
        if(
            len(dados["nome"]) == 0
                or len(dados["celular"]) == 0
                or len(dados["cpf"]) == 0
                or len(dados["especialidade"]) == 0
                or len(dados["registro_profissional"]) == 0
        ):
            self.__view_profissional.mostrar_mensagem("Todos os campos são de preenchimento obrigatório!")
            self.abrir_tela()
        if dados["cpf"] not in self.listar_cpfs_cadastrados():
            try:
                profissional = Profissional(dados["nome"], dados["celular"], dados["cpf"],
                                            dados["especialidade"], dados["registro_profissional"])
                self.__profissionais_dao.add(profissional)
                self.__view_profissional.mostrar_mensagem('Profissional cadastrado(a) com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Profissional de CPF "{dados["cpf"]}" já cadastrado(a)!')

    def excluir_profissional(self):
        profissionais = self.profissionais()
        if len(profissionais) == 0:
            self.__view_profissional.mostrar_mensagem('Nenhum profissional cadastrado!')
            self.abrir_tela()
        cpf = self.__view_profissional.pegar_cpf(profissionais)
        if cpf == None:
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            self.__profissionais_dao.remove(cpf)
            self.__view_profissional.mostrar_mensagem(f'Profissional de CPF "{cpf}" excluído(a)!')
            # Excluir tambem o vinculo com as clinicas
            controlador_clinica = self.__controller_sistema.controller_clinica
            for cnpj in controlador_clinica.listar_cnpjs_cadastrados():
                msg = controlador_clinica.desvincular_profissional_das_clinicas(cnpj, cpf)
                if msg != None:
                    self.__view_profissional.mostrar_mensagem(msg)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{cpf}".')

    def atualizar_nome(self):
        profissionais = self.profissionais()
        if len(profissionais) == 0:
            self.__view_profissional.mostrar_mensagem('Nenhum profissional cadastrado!')
            self.abrir_tela()
        cpf = self.__view_profissional.pegar_cpf(profissionais)
        if cpf == None:
            self.abrir_tela()
        profissional = profissionais[cpf]
        nome_anterior = profissional.nome
        novo_nome = self.__view_profissional.pegar_novo_nome(nome_anterior)
        if novo_nome == None:
            self.abrir_tela()
        if len(novo_nome) == 0:
            self.__view_profissional.mostrar_mensagem('Obrigatório preencher Nome!')
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            try:
                profissional.nome = novo_nome
                self.__profissionais_dao.update(profissional)
                self.__view_profissional.mostrar_mensagem('Nome atualizado!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{cpf}".')

    def atualizar_celular(self):
        profissionais = self.profissionais()
        if len(profissionais) == 0:
            self.__view_profissional.mostrar_mensagem('Nenhum profissional cadastrado!')
            self.abrir_tela()
        cpf = self.__view_profissional.pegar_cpf(profissionais)
        if cpf == None:
            self.abrir_tela()
        profissional = profissionais[cpf]
        celular_anterior = profissional.celular
        novo_celular = self.__view_profissional.pegar_novo_celular(celular_anterior)
        if novo_celular == None:
            self.abrir_tela()
        if len(novo_celular) == 0:
            self.__view_profissional.mostrar_mensagem('Obrigatório preencher Celular!')
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            try:
                profissional.celular = novo_celular
                self.__profissionais_dao.update(profissional)
                self.__view_profissional.mostrar_mensagem('Celular atualizado!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{cpf}".')

    def atualizar_especialidade(self):
        profissionais = self.profissionais()
        if len(profissionais) == 0:
            self.__view_profissional.mostrar_mensagem('Nenhum profissional cadastrado!')
            self.abrir_tela()
        cpf = self.__view_profissional.pegar_cpf(profissionais)
        if cpf == None:
            self.abrir_tela()
        profissional = profissionais[cpf]
        especialidade_anterior = profissional.especialidade
        nova_especialidade = self.__view_profissional.pegar_nova_especialidade(especialidade_anterior)
        if nova_especialidade == None:
            self.abrir_tela()
        if len(nova_especialidade) == 0:
            self.__view_profissional.mostrar_mensagem('Obrigatório preencher Especialidade!')
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            try:
                profissional.especialidade = nova_especialidade
                self.__profissionais_dao.update(profissional)
                self.__view_profissional.mostrar_mensagem('Especialidade atualizada!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{cpf}".')

    def atualizar_registro_profissional(self):
        profissionais = self.profissionais()
        if len(profissionais) == 0:
            self.__view_profissional.mostrar_mensagem('Nenhum profissional cadastrado!')
            self.abrir_tela()
        cpf = self.__view_profissional.pegar_cpf(profissionais)
        if cpf == None:
            self.abrir_tela()
        profissional = profissionais[cpf]
        registro_anterior = profissional.registro_profissional
        novo_registro_profissional = self.__view_profissional.pegar_novo_registro_profissional(registro_anterior)
        if novo_registro_profissional == None:
            self.abrir_tela()
        if len(novo_registro_profissional) == 0:
            self.__view_profissional.mostrar_mensagem('Obrigatório preencher Registro Profissional!')
            self.abrir_tela()
        if cpf in self.listar_cpfs_cadastrados():
            try:
                profissional.registro_profissional = novo_registro_profissional
                self.__profissionais_dao.update(profissional)
                self.__view_profissional.mostrar_mensagem('Registro profissional atualizado!')
            except TipoParametroIncorretoException as e:
                self.__view_profissional.mostrar_mensagem(e)
        else:
            self.__view_profissional.mostrar_mensagem(f'Não há profissional cadastrado(a) com o CPF "{cpf}".')

    def corrigir_cpf(self):
        profissionais = self.profissionais()
        if len(profissionais) == 0:
            self.__view_profissional.mostrar_mensagem('Nenhum profissional cadastrado!')
            self.abrir_tela()
        cpf = self.__view_profissional.pegar_cpf(profissionais)
        if cpf == None:
            self.abrir_tela()
        profissional = profissionais[cpf]
        cpf_cadastrado = profissional.cpf
        cpf_correto = self.__view_profissional.pegar_cpf_correto(cpf_cadastrado)
        if cpf_correto == None:
            self.abrir_tela()
        if len(cpf_correto) == 0:
            self.__view_profissional.mostrar_mensagem('Obrigatório preencher CPF!')
            self.abrir_tela()
        if cpf_correto not in self.listar_cpfs_cadastrados():
            if cpf_cadastrado in self.listar_cpfs_cadastrados():
                try:
                    profissional.cpf = cpf_correto
                    self.__profissionais_dao.remove(cpf_cadastrado)
                    self.__profissionais_dao.add(profissional)
                    self.__view_profissional.mostrar_mensagem("CPF corrigido com sucesso!")
                except TipoParametroIncorretoException as e:
                    self.__view_profissional.mostrar_mensagem(e)
            else:
                msg = f'Não há profissional cadastrado(a) com o CPF "{cpf_cadastrado}".'
                self.__view_profissional.mostrar_mensagem(msg)
        else:
            msg = f'Já existe profissional com o CPF "{cpf_correto}" cadastrado!'
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
