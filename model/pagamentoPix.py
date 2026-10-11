from abstractPagamento import AbstractPagamento
from model.atendimento import Atendimento
from datetime import date as Date
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class PagamentoPix(AbstractPagamento):
    def __init__(self, paciente: str, atendimento: Atendimento, data: Date, valor_pago: float, cpf_pagador: str):
        super().__init__()
        self.paciente = paciente
        self.atendimento = atendimento
        self.data = data
        self.valor_pago = valor_pago
        self.__modalidade = "pix"
        self.cpf_pagador = cpf_pagador

    @property
    def data(self) -> Date:
        return self.__data

    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
        else:
            raise TipoParametroIncorretoException("data")

    @property
    def valor_pago(self) -> float:
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago:float):
        if isinstance(valor_pago, float):
            self.__valor_pago = valor_pago
        else:
            raise TipoParametroIncorretoException("float")

    @property
    def paciente(self) -> str:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: str):
        if isinstance(paciente, str):
            self.__paciente = paciente
        else:
            raise TipoParametroIncorretoException("string")

    @property
    def atendimento(self) -> Atendimento:
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        if isinstance(atendimento, Atendimento):
            self.__atendimento = atendimento
        else:
            raise TipoParametroIncorretoException("Atendimento")

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
