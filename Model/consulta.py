from abstractTipoDeAtendimento import AbstractTipoDeAtendimento


class Consulta(AbstractTipoDeAtendimento):
    def __init__(self, preco:float):
        super().__init__()
        self.preco = preco

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco:float):
        if isinstance(preco, float):
            self.__preco = preco
        else:
            raise TipoParametroIncorretoException("float")
