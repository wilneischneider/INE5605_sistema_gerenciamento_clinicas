from abc import ABC, abstractmethod


class AbstractTipoDeAtendimento(ABC):
    @property
    @abstractmethod
    def tipo_atendimento(self) -> str:
        pass

    @property
    @abstractmethod
    def preco(self) -> float:
        pass

    @preco.setter
    @abstractmethod
    def preco(self, preco:float):
        pass
