class TipoDeAtendimento:
    def __init__(self, descricao:str, preco:float):
        self.descricao = descricao
        self.preco = preco

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao:str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TipoParametroIncorretoException("string")

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco:float):
        if isinstance(preco, float):
            self.__preco = preco
        else:
            raise TipoParametroIncorretoException("float")
