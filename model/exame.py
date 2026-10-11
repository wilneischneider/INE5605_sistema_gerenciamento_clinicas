from abstractTipoDeAtendimento import AbstractTipoDeAtendimento
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class Exame(AbstractTipoDeAtendimento):
    def __init__(self, preco:float):
        super().__init__()
        self.__tipo_atendimento = "exame"
        self.preco = preco

    @property
    def tipo_atendimento(self) -> str:
        return self.__tipo_atendimento

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco:float):
        if isinstance(preco, float):
            self.__preco = preco
        else:
            raise TipoParametroIncorretoException("float")
