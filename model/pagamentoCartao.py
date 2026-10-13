from abstractPagamento import AbstractPagamento
from model.atendimento import Atendimento
from datetime import date as Date
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class PagamentoCartao(AbstractPagamento):
    def __init__(self, paciente: Paciente, atendimento: Atendimento, data: Date,
                 valor_pago: float, cpf_pagador: str, numero_cartao: str,
                 bandeira_cartao: str, numero_parcelas: int= 1):
        super().__init__(paciente, atendimento, data, valor_pago, numero_parcelas)
        self.__modalidade = "Cartao"
        self.cpf_pagador = cpf_pagador
        self.numero_cartao = numero_cartao
        self.bandeira_cartao = bandeira_cartao

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

    @property
    def numero_cartao(self) -> str:
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        if isinstance(numero_cartao, str):
            self.__numero_cartao = numero_cartao
        else:
            raise TipoParametroIncorretoException("string")

    @property
    def bandeira_cartao(self) -> str:
        return self.__bandeira_cartao

    @bandeira_cartao.setter
    def bandeira_cartao(self, bandeira_cartao: str):
        if isinstance(bandeira_cartao, str):
            self.__bandeira_cartao = bandeira_cartao
        else:
            raise TipoParametroIncorretoException("string")
