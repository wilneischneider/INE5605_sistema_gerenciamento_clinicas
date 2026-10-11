from abstractTipoDeAtendimento import AbstractTipoDeAtendimento
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class Retorno(AbstractTipoDeAtendimento):
    def __init__(self, preco:float= 0):
        super().__init__()
        self.__tipo_atendimento = "retorno"
        self.preco = preco

    @property
    def tipo_atendimento(self) -> str:
        return self.__tipo_atendimento

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco:float= 0):
        if isinstance(preco, float):
            self.__preco = 0
        else:
            raise TipoParametroIncorretoException("float")
