from abc import ABC, abstractmethod
from datetime import date as Date
from model.atendimento import Atendimento


class AbstractPagamento(ABC):
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
    def paciente(self) -> str:
        pass

    @paciente.setter
    @abstractmethod
    def paciente(self, paciente: str):
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

    @modalidade.setter
    @abstractmethod
    def modalidade(self, modalidade: str):
        pass

    @property
    @abstractmethod
    def cpf_pagador(self) -> str:
        pass

    @cpf_pagador.setter
    @abstractmethod
    def cpf_pagador(self, cpf_pagador: str):
        pass

    @property
    @abstractmethod
    def numero_cartao(self) -> str:
        pass

    @numero_cartao.setter
    @abstractmethod
    def numero_cartao(self, numero_cartao: str):
        pass

    @property
    @abstractmethod
    def bandeira_cartao(self) -> str:
        pass

    @bandeira_cartao.setter
    @abstractmethod
    def bandeira_cartao(self, bandeira_cartao: str):
        pass

    @property
    @abstractmethod
    def numero_parcelas(self) -> int:
        pass

    @numero_parcelas.setter
    @abstractmethod
    def numero_parcelas(self, numero_parcelas: int):
        pass
