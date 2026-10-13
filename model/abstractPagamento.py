from abc import ABC, abstractmethod
from datetime import date as Date
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from model.atendimento import Atendimento
from model.paciente import Paciente


class AbstractPagamento(ABC):
    @abstractmethod
    def __init__(self, paciente: Paciente, atendimento: Atendimento, data: Date,
                 valor_pago: float, numero_parcelas: int):
        self.paciente = paciente
        self.atendimento = atendimento
        self.data = data
        self.valor_pago = valor_pago
        self.numero_parcelas = numero_parcelas

    @property
    @abstractmethod
    def data(self) -> Date:
        return self.__data

    @data.setter
    @abstractmethod
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
        else:
            TipoParametroIncorretoException("Data")

    @property
    @abstractmethod
    def valor_pago(self) -> float:
        return self.__valor_pago

    @valor_pago.setter
    @abstractmethod
    def valor_pago(self, valor_pago:float):
        if isinstance(valor_pago, float):
            self.__valor_pago = valor_pago
        else:
            TipoParametroIncorretoException("float")

    @property
    @abstractmethod
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    @abstractmethod
    def paciente(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        else:
            TipoParametroIncorretoException("Paciente")

    @property
    @abstractmethod
    def atendimento(self) -> Atendimento:
        return self.__atendimento

    @atendimento.setter
    @abstractmethod
    def atendimento(self, atendimento: Atendimento):
        if isinstance(atendimento, Atendimento):
            self.__atendimento = atendimento
        else:
            TipoParametroIncorretoException("Atendimento")

    @property
    @abstractmethod
    def modalidade(self) -> str:
        pass

    @property
    @abstractmethod
    def numero_parcelas(self) -> int:
        return self.__numero_parcelas

    @numero_parcelas.setter
    @abstractmethod
    def numero_parcelas(self, numero_parcelas: int):
        if isinstance(numero_parcelas, int):
            self.__numero_parcelas = numero_parcelas
        else:
            TipoParametroIncorretoException("int")
