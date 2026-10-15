from abc import ABC, abstractmethod
from datetime import date as Date
from model.atendimento import Atendimento
from model.paciente import Paciente


class AbstractPagamento(ABC):
    @abstractmethod
    def __init__(self, paciente: Paciente, atendimento: Atendimento, data: Date,
                 valor_pago: float, numero_parcelas: int):
        pass

    @property
    @abstractmethod
    def data(self) -> Date:
        pass

    @data.setter
    @abstractmethod
    def data(self, data: Date):
        pass

    @property
    @abstractmethod
    def valor_pago(self) -> float:
        pass

    @valor_pago.setter
    @abstractmethod
    def valor_pago(self, valor_pago:float):
        pass

    @property
    @abstractmethod
    def paciente(self) -> Paciente:
        pass

    @paciente.setter
    @abstractmethod
    def paciente(self, paciente: Paciente):
        pass

    @property
    @abstractmethod
    def atendimento(self) -> Atendimento:
        pass

    @atendimento.setter
    @abstractmethod
    def atendimento(self, atendimento: Atendimento):
        pass

    @property
    @abstractmethod
    def modalidade(self) -> str:
        pass

    @property
    @abstractmethod
    def numero_parcelas(self) -> int:
        pass

    @numero_parcelas.setter
    @abstractmethod
    def numero_parcelas(self, numero_parcelas: int):
        pass
