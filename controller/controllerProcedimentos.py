from model.procedimento import Procedimento
from exceptions.procedimentoJaCadastradoException import ProcedimentoJaCadastradoException
from exceptions.procedimentoNaoEncontradoException import ProcedimentoNaoEncontradoException
from model.profissional import Profissional


class ControllerProcedimento:
    def __init__(self):
        self.__procedimentos = {}

    def listar_procedimentos_cadastrados(self):
        return self.__procedimentos.values()

    def listar_descricao_procedimentos_cadastrados(self):
        return self.__procedimentos.keys()

    def retornar_procedimento(self, descricao:str) -> Procedimento:
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            return self.__procedimentos[descricao]
        else:
            raise ProcedimentoNaoEncontradoException(descricao)

    def cadastrar_procedimento(self, descricao:str, custo: float, profissional:Profissional):
        if descricao not in self.listar_descricao_procedimentos_cadastrados():
            procedimento = Procedimento(descricao, custo, profissional)
            self.__procedimentos.update({descricao: procedimento})
            return True
        else:
            raise ProcedimentoJaCadastradoException(descricao)

    def excluir_procedimento(self, descricao):
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            self.__procedimentos.pop(descricao)
            return True
        else:
            raise ProcedimentoNaoEncontradoException(descricao)

    def alterar_custo_procedimento(self, descricao:str, custo:float):
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            self.__procedimentos[descricao].custo = custo
            return True
        else:
            raise ProcedimentoNaoEncontradoException(descricao)

    def alterar_profissional_responsavel(self, descricao:str, profissional:Profissional):
        if descricao in self.listar_descricao_procedimentos_cadastrados():
            self.__procedimentos[descricao].profissional = profissional
            return True
        else:
            raise ProcedimentoNaoEncontradoException(descricao)

    def corrigir_descricao_procedimento(self, descricao_correta:str, descricao_cadastrada:str):
        if descricao_correta not in self.listar_descricao_procedimentos_cadastrados():
            if descricao_cadastrada in self.listar_descricao_procedimentos_cadastrados():
                procedimento = self.__procedimentos[descricao_cadastrada]
                procedimento.descricao = descricao_correta
                self.__procedimentos.pop(descricao_cadastrada)
                self.__procedimentos.update({descricao_correta: procedimento})
                return True
            else:
                raise ProcedimentoNaoEncontradoException(descricao_cadastrada)
        else:
            raise ProcedimentoJaCadastradoException(descricao_correta)
