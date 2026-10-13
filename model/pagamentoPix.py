from abstractPagamento import AbstractPagamento
from model.atendimento import Atendimento
from datetime import date as Date
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class PagamentoPix(AbstractPagamento):
    def __init__(self, paciente: Paciente, atendimento: Atendimento, data: Date,
                 valor_pago: float, cpf_pagador: str, numero_parcelas: int= 1):
        super().__init__(paciente, atendimento, data, valor_pago, numero_parcelas)
        self.__modalidade = "Pix"
        self.cpf_pagador = cpf_pagador

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
