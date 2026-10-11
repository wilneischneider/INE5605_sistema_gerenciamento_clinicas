from datetime import date as Date
from datetime import time as Time
from model.abstractTipoDeAtendimento import AbstractTipoDeAtendimento
from model.paciente import Paciente
from model.clinica import Clinica
from model.profissional import Profissional


class Atendimento:
    def __init__(
            self,
            clinica:Clinica,
            paciente:Paciente,
            profissional:Profissional,
            data:Date,
            horario_inicio:Time,
            horario_fim:Time,
            tipo_de_atendimento: AbstractTipoDeAtendimento
    ):
        self.clinica = clinica
        self.paciente = paciente
        self.profissional = profissional
        self.data = data
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.tipo_de_atendimento = tipo_de_atendimento
        self.__procedimentos_realizados = []
        self.__responsavel = None

    @property
    def clinica(self) -> Clinica:
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica:Clinica):
        if isinstance(clinica, Clinica):
            self.__clinica = clinica
        else:
            raise TipoParametroIncorretoException("Clinica")

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        else:
            raise TipoParametroIncorretoException("Paciente")

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional):
        if isinstance(profissional, Profissional):
            self.__profissional = profissional
        else:
            raise TipoParametroIncorretoException("Profissional")

    @property
    def data(self) -> Date:
        return self.__data

    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
        else:
            raise TipoParametroIncorretoException("Data")

    @property
    def horario_inicio(self) -> Time:
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: Time):
        if isinstance(horario_inicio, Time):
            self.__horario_inicio = horario_inicio
        else:
            raise TipoParametroIncorretoException("Hora")

    @property
    def horario_fim(self) -> Time:
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: Time):
        if isinstance(horario_fim, Time):
            self.__horario_fim = horario_fim
        else:
            raise TipoParametroIncorretoException("Hora")

    @property
    def tipo_de_atendimento(self) -> AbstractTipoDeAtendimento:
        return self.__tipo_de_atendimento

    @tipo_de_atendimento.setter
    def tipo_de_atendimento(self, tipo_de_atendimento: AbstractTipoDeAtendimento):
        if isinstance(tipo_de_atendimento, AbstractTipoDeAtendimento):
            self.__tipo_de_atendimento = tipo_de_atendimento
        else:
            raise TipoParametroIncorretoException("AbstractTipoDeAtendimento")

    @property
    def procedimentos_realizados(self) -> list:
        return self.__procedimentos_realizados

    @property
    def responsavel(self) -> Pessoa:
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, responsavel: Pessoa):
        if isinstance(responsavel, Pessoa):
            self.__responsavel = responsavel
        else:
            raise TipoParametroIncorretoException("Pessoa")
