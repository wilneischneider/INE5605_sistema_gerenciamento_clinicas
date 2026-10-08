from Model.tipoParametroIncorretoException import TipoParametroIncorretoException


class Clinica:
    def __init__(self, nome:str, cidade: str, descricao:str):
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TipoParametroIncorretoException("string")

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade
        else:
            raise TipoParametroIncorretoException("string")

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TipoParametroIncorretoException("string")
