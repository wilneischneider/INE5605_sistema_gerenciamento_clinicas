from model.abstractPagamento import AbstractPagamento
from model.atendimento import Atendimento
from model.paciente import Paciente
from datetime import date as Date


class PagamentoDinheiro(AbstractPagamento):
    def __init__(self, paciente: Paciente, atendimento: Atendimento, data: Date,
                 valor_pago: float, numero_parcelas: int= 1):
        super().__init__(paciente, atendimento, data, valor_pago, numero_parcelas)
        self.__modalidade = "Dinheiro"

    @property
    def modalidade(self) -> str:
        return self.__modalidade
