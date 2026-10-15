from model.abstractPagamento import AbstractPagamento
from model.atendimento import Atendimento
from model.paciente import Paciente
from datetime import date as Date
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class PagamentoPix(AbstractPagamento):
    def __init__(self, paciente: Paciente, atendimento: Atendimento, data: Date,
                 valor_pago: float, cpf_pagador: str, numero_parcelas: int= 1):
        self.paciente = paciente
        self.atendimento = atendimento
        self.data = data
        self.valor_pago = valor_pago
        self.numero_parcelas = numero_parcelas
        self.__modalidade = "Pix"
        self.cpf_pagador = cpf_pagador

    @property
    def data(self) -> Date:
        return self.__data

    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
        else:
            TipoParametroIncorretoException("Data")

    @property
    def valor_pago(self) -> float:
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        if isinstance(valor_pago, float):
            self.__valor_pago = valor_pago
        else:
            TipoParametroIncorretoException("float")

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        else:
            TipoParametroIncorretoException("Paciente")

    @property
    def atendimento(self) -> Atendimento:
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        if isinstance(atendimento, Atendimento):
            self.__atendimento = atendimento
        else:
            TipoParametroIncorretoException("Atendimento")

    @property
    def numero_parcelas(self) -> int:
        return self.__numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, numero_parcelas: int):
        if isinstance(numero_parcelas, int):
            self.__numero_parcelas = numero_parcelas
        else:
            TipoParametroIncorretoException("int")

    @property
    def modalidade(self) -> str:
        return self.__modalidade

    @property
    def cpf_pagador(self) -> str:
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        if isinstance(cpf_pagador, str):
            self.__cpf_pagador = cpf_pagador
        else:
            raise TipoParametroIncorretoException("string")
