import datetime

from Model.tipoParametroIncorretoException import TipoParametroIncorretoException
from Model.pessoa import Pessoa
from datetime import date as Date


class Paciente(Pessoa):
    def __init__(self, nome:str, celular: str, cpf:str, data_de_nascimento: Date):
        super().__init__(nome, celular, cpf)
        self.data_de_nascimento = data_de_nascimento

    @property
    def data_de_nascimento (self) -> Date:
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento: Date):
        if isinstance(data_de_nascimento, Date):
            self.__data_de_nascimento = data_de_nascimento
        else:
            raise TipoParametroIncorretoException("data")

    def calcular_idade(self) -> int:
        idade = Date.today() - self.__data_de_nascimento
        return datetime.timedelta()

print(datetime.timedelta(Date.today() - Date(1989, 10, 9)))