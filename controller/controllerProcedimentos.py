from model.pessoa import Pessoa
from model.procedimento import Procedimento
from view.viewProcedimentos import ViewProcedimentos
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from daos.daoProcedimentos import DaoProcedimentos


class ControllerProcedimento:
    def __init__(self, controller_sistema):
        self.__procedimentos_dao = DaoProcedimentos()
        self.__controller_sistema = controller_sistema
        self.__view_procedimento = ViewProcedimentos()

    def procedimentos(self):
        return self.__procedimentos_dao.get_dict()

    def listar_procedimentos_cadastrados(self):
        lista_dados = []
        for procedimento in self.__procedimentos_dao.get_all():
            registro = {"descricao": procedimento.descricao, "custo": procedimento.custo,
                        "profissional": procedimento.profissional.nome}
            lista_dados.append(registro)
        self.__view_procedimento.mostrar_dados_procedimento(lista_dados)

    def listar_descricao_procedimentos_cadastrados(self):
        procedimentos = self.__procedimentos_dao.get_dict()
        return list(procedimentos.keys())

    def retornar_procedimento(self):
        procedimentos = self.procedimentos()
        descricao = self.__view_procedimento.pegar_descricao(procedimentos)
        if descricao == None:
            self.abrir_tela()
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            procedimento = procedimentos[descricao]
            lista_dados = [{"descricao": procedimento.descricao, "custo": procedimento.custo,
                            "profissional": procedimento.profissional.nome}]
            self.__view_procedimento.mostrar_dados_procedimento(lista_dados)
        else:
            self.__view_procedimento.mostrar_mensagem(f'Não há procedimento com a descrição "{descricao}"!')

    def cadastrar_procedimento(self):
        controlador_profissional = self.__controller_sistema.controller_profissional
        dados = self.__view_procedimento.pegar_dados_procedimento()
        if dados == None:
            self.abrir_tela()
        if len(dados["descricao"]) == 0:
            self.__view_procedimento.mostrar_mensagem("Obrigatório o preenchimento de todos os campos!")
            self.abrir_tela()
        profissionais = controlador_profissional.profissionais()
        cpf_profissional = self.__view_procedimento.pegar_cpf(profissionais)
        if cpf_profissional == None:
            self.abrir_tela()
        if dados["descricao"] not in self.listar_descricao_procedimentos_cadastrados():
            if cpf_profissional in controlador_profissional.listar_cpfs_cadastrados():
                try:
                    profissional = profissionais[cpf_profissional]
                    procedimento = Procedimento(dados["descricao"], dados["custo"], profissional)
                    self.__procedimentos_dao.add(procedimento)
                except TipoParametroIncorretoException as e:
                    self.__view_procedimento.mostrar_mensagem(e)
            else:
                msg = f'Não há profissional cadastrado com o CPF "{cpf_profissional}"!'
                self.__view_procedimento.mostrar_mensagem(msg)
        else:
            msg = f'Já existe procedimento cadastrado com a descrição "{dados["descricao"]}"!'
            self.__view_procedimento.mostrar_mensagem(msg)

    def excluir_procedimento(self):
        procedimentos = self.procedimentos()
        descricao = self.__view_procedimento.pegar_descricao(procedimentos)
        if descricao == None:
            self.abrir_tela()
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            self.__procedimentos_dao.remove(descricao)
            self.__view_procedimento.mostrar_mensagem('Procedimento excluído com sucesso!')
        else:
            self.__view_procedimento.mostrar_mensagem(f'Não há procedimento com a descrição "{descricao}"!')

    def alterar_custo_procedimento(self):
        procedimentos = self.procedimentos()
        descricao = self.__view_procedimento.pegar_descricao(procedimentos)
        if descricao == None:
            self.abrir_tela()
        procedimento = procedimentos[descricao]
        custo_atual = procedimento.custo
        novo_custo = self.__view_procedimento.pegar_novo_custo(custo_atual)
        if novo_custo == None:
            self.abrir_tela()
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            try:
                procedimento.custo = novo_custo
                self.__procedimentos_dao.update(procedimento)
                self.__view_procedimento.mostrar_mensagem('Custo do procedimento atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_procedimento.mostrar_mensagem(e)
        else:
            self.__view_procedimento.mostrar_mensagem(f'Não há procedimento com a descrição "{descricao}"!')

    def alterar_profissional_responsavel(self):
        procedimentos = self.procedimentos()
        descricao = self.__view_procedimento.pegar_descricao(procedimentos)
        if descricao == None:
            self.abrir_tela()
        procedimento = procedimentos[descricao]
        profissional_atual = procedimento.profissional.nome
        controlador_profissional = self.__controller_sistema.controller_profissional
        profissionais = controlador_profissional.profissionais()
        cpf_profissional = self.__view_procedimento.pegar_novo_profissional(profissional_atual, profissionais)
        if cpf_profissional == None:
            self.abrir_tela()
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            if cpf_profissional in controlador_profissional.listar_cpfs_cadastrados():
                try:
                    profissional = profissionais[cpf_profissional]
                    procedimento.profissional = profissional
                    self.__procedimentos_dao.update(procedimento)
                    self.__view_procedimento.mostrar_mensagem('Profissional do procedimento atualizado com sucesso!')
                except TipoParametroIncorretoException as e:
                    self.__view_procedimento.mostrar_mensagem(e)
            else:
                msg = f'Não há profissional cadastrado com o CPF "{cpf_profissional}"!'
                self.__view_procedimento.mostrar_mensagem(msg)
        else:
            self.__view_procedimento.mostrar_mensagem(f'Não há procedimento com a descrição "{descricao}"!')

    def corrigir_descricao_procedimento(self):
        procedimentos = self.procedimentos()
        descricao_cadastrada = self.__view_procedimento.pegar_descricao(procedimentos)
        if descricao_cadastrada == None:
            self.abrir_tela()
        procedimento = procedimentos[descricao_cadastrada]
        descricao_correta = self.__view_procedimento.pegar_descricao_correta(procedimento.descricao)
        if descricao_correta == None:
            self.abrir_tela()
        if len(descricao_correta) == 0:
            self.__view_procedimento.mostrar_mensagem("Obrigatório informar a descrição do procedimento!")
            self.abrir_tela()
        if descricao_correta not in self.listar_descricao_procedimentos_cadastrados():
            if descricao_cadastrada in self.listar_descricao_procedimentos_cadastrados():
                try:
                    procedimento.descricao = descricao_correta
                    self.__procedimentos_dao.remove(descricao_cadastrada)
                    self.__procedimentos_dao.add(procedimento)
                except TipoParametroIncorretoException as e:
                    self.__view_procedimento.mostrar_mensagem(e)
            else:
                msg = f'Não há procedimento com a descrição "{descricao_cadastrada}".'
                self.__view_procedimento.mostrar_mensagem(msg)
        else:
            msg = f'Já existe procedimento cadastrado com a descrição "{descricao_correta}".'
            self.__view_procedimento.mostrar_mensagem(msg)

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.cadastrar_procedimento, 2: self.retornar_procedimento,
                  3: self.listar_procedimentos_cadastrados, 4: self.excluir_procedimento,
                  5: self.alterar_custo_procedimento, 6: self.alterar_profissional_responsavel,
                  7: self.corrigir_descricao_procedimento}
        while True:
            opcoes[self.__view_procedimento.view_opcoes()]()
