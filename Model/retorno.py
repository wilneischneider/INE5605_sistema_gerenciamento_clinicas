from abstractTipoDeAtendimento import AbstractTipoDeAtendimento


class Retorno(AbstractTipoDeAtendimento):
    def __init__(self, preco:float = 0):
        super().__init__()
        self.preco = preco

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco:float= 0):
        if isinstance(preco, float):
            self.__preco = 0
        else:
            raise TipoParametroIncorretoException("float")
