from Model.tipoParametroIncorretoException import TipoParametroIncorretoException
from datetime import time as Time


class Clinica:
    def __init__(
            self,
            cnpj:str,
            nome:str,
            cidade: str,
            descricao:str,
            horario_de_abertura:Time,
            horario_de_fechamento:Time
    ):
        self.cnpj = cnpj
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao
        self.horario_de_abertura = horario_de_abertura
        self.horario_de_fechamento = horario_de_fechamento
        self.__profissionais = []

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
        else:
            raise TipoParametroIncorretoException("string")

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

    @property
    def horario_de_abertura(self) -> Time:
        return self.__horario_de_abertura

    @horario_de_abertura.setter
    def horario_de_abertura(self, horario_de_abertura: Time):
        if isinstance(horario_de_abertura, Time):
            self.__horario_de_abertura = horario_de_abertura
        else:
            raise TipoParametroIncorretoException("Hora")

    @property
    def horario_de_fechamento(self) -> Time:
        return self.__horario_de_fechamento

    @horario_de_fechamento.setter
    def horario_de_fechamento(self, horario_de_fechamento: Time):
        if isinstance(horario_de_fechamento, Time):
            self.__horario_de_fechamento = horario_de_fechamento
        else:
            raise TipoParametroIncorretoException("Hora")

    @property
    def profissionais(self) -> list:
        return self.__profissionais

    def vincular_profissional(self, cpf:str):
        if isinstance(cpf, str):
            self.__profissionais.append(cpf)
        else:
            raise TipoParametroIncorretoException("string")

    def desvincular_profissional(self, cpf:str):
        if isinstance(cpf, str):
            self.__profissionais.remove(cpf)
        else:
            raise TipoParametroIncorretoException("string")
