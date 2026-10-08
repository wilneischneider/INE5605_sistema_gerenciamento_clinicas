from Model.profissional import Profissional
from tipoParametroIncorretoException import TipoParametroIncorretoException


class Procedimento:
    def __init__(self, descricao:str, custo:float, profissional:Profissional):
        self.descricao = descricao
        self.custo = custo
        self.profissional = profissional

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TipoParametroIncorretoException("string")

    @property
    def custo(self) -> float:
        return self.__custo

    @custo.setter
    def custo(self, custo: float):
        if isinstance(custo, float):
            self.__custo = custo
        else:
            raise TipoParametroIncorretoException("float")

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional):
        if isinstance(profissional, Profissional):
            self.__profissional = profissional
        else:
            raise TipoParametroIncorretoException("Profissional")
