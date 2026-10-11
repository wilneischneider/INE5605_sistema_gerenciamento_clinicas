from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class Pessoa:
    def __init__(self, nome:str, celular: str, cpf:str):
        self.nome = nome
        self.celular = celular
        self.cpf = cpf

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
    def celular(self) -> str:
        return self.__celular

    @celular.setter
    def celular(self, celular: str):
        if isinstance(celular, str):
            self.__celular = celular
        else:
            raise TipoParametroIncorretoException("string")

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf
        else:
            raise TipoParametroIncorretoException("string")
