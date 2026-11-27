from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from view.viewTiposDeAtendimento import ViewTiposDeAtendimento
from model.tipoDeAtendimento import TipoDeAtendimento
from daos.daoTiposDeAtendimento import DaoTipoDeAtendimento


class ControllerTipoDeAtendimento:
    def __init__(self, controller_sistema):
        self.__tipos_de_atendimento_dao = DaoTipoDeAtendimento()
        self.__controller_sistema = controller_sistema
        self.__view_tipos_de_atendimento = ViewTiposDeAtendimento()

    def tipos_de_atendimento(self):
        return self.__tipos_de_atendimento_dao.get_all()

    def listar_descricao_tipos_atendimento(self):
        descricao = []
        tipos_de_atendimento = self.tipos_de_atendimento()
        for objeto in tipos_de_atendimento:
            descricao.append(objeto.tipo)
        return descricao

    def listar_tipos_de_atendimento(self):
        self.__view_tipos_de_atendimento.mostrar_tipos_atendimento(self.listar_descricao_tipos_atendimento())

    def cadastrar_tipo_atendimento(self):
        tipo = self.__view_tipos_de_atendimento.pegar_dados_tipo_atendimento()
        if tipo == None:
            self.abrir_tela()
        if len(tipo) == 0:
            self.__view_tipos_de_atendimento.mostrar_mensagem("Obrigatório preencher o tipo do atendimento!")
            self.abrir_tela()
        if tipo not in self.listar_descricao_tipos_atendimento():
            try:
                novo_tipo = TipoDeAtendimento(tipo)
                self.__tipos_de_atendimento_dao.add(novo_tipo)
                self.__view_tipos_de_atendimento.mostrar_mensagem(f'O tipo "{tipo}" foi cadastrado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_tipos_de_atendimento.mostrar_mensagem(e)
        else:
            self.__view_tipos_de_atendimento.mostrar_mensagem(f'O tipo "{tipo}" já está cadastrado!')

    def excluir_tipo_atendimento(self):
        tipos = self.listar_descricao_tipos_atendimento()
        tipo = self.__view_tipos_de_atendimento.pegar_tipo_atendimento(tipos)
        if tipo == None:
            self.abrir_tela()
        if tipo in tipos:
            self.__tipos_de_atendimento_dao.remove(tipo)
            self.__view_tipos_de_atendimento.mostrar_mensagem('Tipo de atendimento excluído com sucesso!')
        else:
            self.__view_tipos_de_atendimento.mostrar_mensagem(f'Não há atendimento do tipo "{tipo}" cadastrado!')

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.listar_tipos_de_atendimento, 2: self.cadastrar_tipo_atendimento,
                  3: self.excluir_tipo_atendimento}
        while True:
            opcoes[self.__view_tipos_de_atendimento.view_opcoes()]()
