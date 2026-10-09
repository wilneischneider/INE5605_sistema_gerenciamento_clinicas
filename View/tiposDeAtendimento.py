from View.tipoDeAtendimento import TipoDeAtendimento
from View.tipoDeAtendimentoNaoEncontradoException import TipoDeAtendimentoNaoEncontradoException
from View.tipoDeAtendimentoJaCadastradoException import TipoDeAtendimentoJaCadastradoException


class ControllerTipoDeAtendimento:
    def __init__(self):
        self.__tipos_de_atendimento = {}

    def listar_tipos_de_atendimento(self) -> list:
        return self.__tipos_de_atendimento.keys()

    def retornar_tipos_de_atendimento(self) -> list:
        return self.__tipos_de_atendimento.values()

    def cadastrar_tipo_de_atendimento(self, descricao:str, preco:float):
        if descricao not in self.listar_tipos_de_atendimento():
            tipo = TipoDeAtendimento(descricao, preco)
            self.__tipos_de_atendimento.update({descricao:tipo})
        else:
            raise TipoDeAtendimentoJaCadastradoException(descricao)

    def excluir_tipo_de_atendimento(self, descricao:str):
        if descricao in self.listar_tipos_de_atendimento():
            self.__tipos_de_atendimento.pop(descricao)
        else:
            raise TipoDeAtendimentoNaoEncontradoException(descricao)

    def atualizar_preco_tipo_atendimento(self, descricao:str, preco_novo:float):
        if descricao in self.listar_tipos_de_atendimento():
            tipo = TipoDeAtendimento(descricao, preco_novo)
            self.__tipos_de_atendimento.update({descricao: tipo})
        else:
            raise TipoDeAtendimentoNaoEncontradoException(descricao)

    def consultar_preco_tipo_atendimento(self, descricao:str):
        if descricao in self.listar_tipos_de_atendimento():
            tipo = self.__tipos_de_atendimento[descricao]
            return tipo.preco
        else:
            raise TipoDeAtendimentoNaoEncontradoException(descricao)
