from controller.controllerProfissionais import ControllerProfissional
from model.procedimento import Procedimento
from exceptions.procedimentoNaoEncontradoException import ProcedimentoNaoEncontradoException
from view.viewProcedimentos import ViewProcedimentos
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class ControllerProcedimento:
    def __init__(self, controller_sistema):
        self.__procedimentos = {}
        self.__controller_sistema = controller_sistema
        self.__view_procedimento = ViewProcedimentos()

    @property
    def procedimentos(self):
        return self.__procedimentos

    def listar_procedimentos_cadastrados(self):
        lista_dados = []
        for procedimento in self.procedimentos.values():
            registro = {"descricao": procedimento.descricao, "custo": procedimento.custo,
                        "profissional": procedimento.profissional.nome}
            lista_dados.append(registro)
        self.__view_procedimento.mostrar_dados_procedimento(lista_dados)

    def listar_descricao_procedimentos_cadastrados(self):
        return self.__procedimentos.keys()

    def retornar_procedimento(self):
        descricao = self.__view_procedimento.pegar_descricao()
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            procedimento = self.procedimentos[descricao]
            lista_dados = [{"descricao": procedimento.descricao, "custo": procedimento.custo,
                            "profissional": procedimento.profissional.nome}]
            self.__view_procedimento.mostrar_dados_procedimento(lista_dados)
        else:
            self.__view_procedimento.mostrar_mensagem(f'Não há procedimento com a descrição "{descricao}"!')


        if descricao in self.listar_descricao_procedimentos_cadastrados():
            return self.__procedimentos[descricao]
        else:
            raise ProcedimentoNaoEncontradoException(descricao)

    def cadastrar_procedimento(self):
        dados = self.__view_procedimento.pegar_dados_procedimento()
        if dados["descricao"] not in self.listar_descricao_procedimentos_cadastrados():
            if dados["cpf_profissional"] in ControllerProfissional.listar_cpfs_cadastrados():
                try:
                    profissional = ControllerProfissional.profissionais[dados["cpf_profissional"]]
                    procedimento = Procedimento(dados["descricao"], dados["custo"], profissional)
                    self.__procedimentos.update({dados["descricao"]: procedimento})
                except TipoParametroIncorretoException as e:
                    self.__view_procedimento.mostrar_mensagem(e)
            else:
                msg = f'Não há profissional cadastrado com o CPF "{dados["cpf_profissional"]}"!'
                self.__view_procedimento.mostrar_mensagem(msg)
        else:
            msg = f'Já existe procedimento cadastrado com a descrição "{dados["descricao"]}"!'
            self.__view_procedimento.mostrar_mensagem(msg)

    def excluir_procedimento(self):
        self.__view_procedimento.mostrar_mensagem('--- Excluir Procedimento ---')
        descricao = self.__view_procedimento.pegar_descricao()
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            self.__procedimentos.pop(descricao)
            self.__view_procedimento.mostrar_mensagem('Procedimento excluído com sucesso!')
        else:
            self.__view_procedimento.mostrar_mensagem(f'Não há procedimento com a descrição "{descricao}"!')

    def alterar_custo_procedimento(self):
        dados = self.__view_procedimento.pegar_novo_custo()
        if dados["descricao"] in self.listar_descricao_procedimentos_cadastrados():
            try:
                procedimento = self.__procedimentos[dados["descricao"]]
                procedimento.custo = dados["custo"]
                self.__procedimentos.update({dados["descricao"]: procedimento})
                self.__view_procedimento.mostrar_mensagem('Custo do procedimento atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_procedimento.mostrar_mensagem(e)
        else:
            self.__view_procedimento.mostrar_mensagem(f'Não há procedimento com a descrição "{dados["descricao"]}"!')

    def alterar_profissional_responsavel(self):
        dados = self.__view_procedimento.pegar_novo_profissional()
        if dados["descricao"] in self.listar_descricao_procedimentos_cadastrados():
            if dados["cpf_profissional"] in ControllerProfissional.listar_cpfs_cadastrados():
                try:
                    profissional = ControllerProfissional.profissionais[dados["cpf_profissional"]]
                    procedimento = self.__procedimentos[dados["descricao"]]
                    procedimento.profissional = profissional
                    self.__procedimentos.update({dados["descricao"]: procedimento})
                    self.__view_procedimento.mostrar_mensagem('Profissional do procedimento atualizado com sucesso!')
                except TipoParametroIncorretoException as e:
                    self.__view_procedimento.mostrar_mensagem(e)
            else:
                msg = f'Não há profissional cadastrado com o CPF "{dados["cpf_profissional"]}"!'
                self.__view_procedimento.mostrar_mensagem(msg)
        else:
            self.__view_procedimento.mostrar_mensagem(f'Não há procedimento com a descrição "{dados["descricao"]}"!')

    def corrigir_descricao_procedimento(self):
        dados = self.__view_procedimento.pegar_descricao_correta()
        if dados["descricao_correta"] not in self.listar_descricao_procedimentos_cadastrados():
            if dados["descricao_cadastrada"] in self.listar_descricao_procedimentos_cadastrados():
                try:
                    procedimento = self.__procedimentos[dados["descricao_cadastrada"]]
                    procedimento.descricao = dados["descricao_correta"]
                    self.__procedimentos.pop(dados["descricao_cadastrada"])
                    self.__procedimentos.update({dados["descricao_correta"]: procedimento})
                except TipoParametroIncorretoException as e:
                    self.__view_procedimento.mostrar_mensagem(e)
            else:
                msg = f'Não há procedimento com a descrição "{dados["descricao_cadastrada"]}".'
                self.__view_procedimento.mostrar_mensagem(msg)
        else:
            msg = f'Já existe procedimento cadastrado com a descrição "{dados["descricao_correta"]}".'
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
