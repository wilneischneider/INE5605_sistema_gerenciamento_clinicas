from abstractPagamento import AbstractPagamento
from model.atendimento import Atendimento
from datetime import date as Date
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class PagamentoCartao(AbstractPagamento):
    def __init__(
            self,
            paciente: str,
            atendimento: Atendimento,
            data: Date,
            valor_pago: float,
            cpf_pagador: str,
            numero_cartao: str,
            bandeira_cartao: str,
            numero_parcelas: int
    ):
        super().__init__()
        self.paciente = paciente
        self.atendimento = atendimento
        self.data = data
        self.valor_pago = valor_pago
        self.__modalidade = "cartao"
        self.cpf_pagador = cpf_pagador
        self.numero_cartao = numero_cartao
        self.bandeira_cartao = bandeira_cartao
        self.numero_parcelas = numero_parcelas

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

    @property
    def numero_parcelas(self) -> int:
        return self.__numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, numero_parcelas: int):
        if isinstance(numero_parcelas, int):
            self.__numero_parcelas = numero_parcelas
        else:
            raise TipoParametroIncorretoException("inteiro")
