from controllerClinicas import ControllerClinica
from controllerPacientes import ControllerPaciente
from controllerProfissionais import ControllerProfissional
from datetime import date as Date
from datetime import time as Time
from model.atendimento import Atendimento
from exceptions.pacienteMenorDeIdadeException import PacienteMenorDeIdadeException
from exceptions.horarioForaDoHorarioDaClinaException import HorarioForaDoHorarioDaClinicaException

class ControllerAtendimento:
    def __init__(self):
        self.__atendimentos = []

    def listar_atendimentos(self) -> list:
        return self.__atendimentos

    def agendar_atendimento(
            self,
            cnpj:str,
            cpf_paciente:str,
            cpf_profissional:str,
            data: Date,
            horario_inicio: Time,
            horario_fim: Time,
            tipo_de_atendimento
    ):
        clinica = ControllerClinica.retornar_clinica(cnpj)
        if (
            clinica.horario_de_abertura <= horario_inicio
            and clinica.horario_de_fechamento >= horario_fim
            and horario_fim > horario_inicio
        ):
            paciente = ControllerPaciente.retornar_paciente(cpf_paciente)
            profissional = ControllerProfissional.retornar_profissional(cpf_profissional)
            if ControllerPaciente.calcular_idade_paciente(paciente.cpf) >= 18:
                atendimento = Atendimento(
                    clinica,
                    paciente,
                    profissional,
                    data,
                    horario_inicio,
                    horario_fim,
                    tipo_de_atendimento
                )
                self.__atendimentos.append(atendimento)
            else:
                raise PacienteMenorDeIdadeException()
        else:
            horario_da_clinica = {"abre":clinica.horario_de_abertura, "fecha": clinica.horario_de_fechamento}
            raise HorarioForaDoHorarioDaClinicaException(horario_da_clinica)

    def cancelar_atendimento(self): #implementar se der tempo
        pass


    #COPIADO PARA CÁ, PRECISA AJUSTAR O CODIGO
    def adicionar_procedimento(self, descricao:str):
        if descricao in ControllerProcedimento.listar_descricao_procedimentos_cadastrados():
            procedimento = ControllerProcedimento.retornar_procedimento(descricao)
            self.__procedimentos_realizados.append(procedimento)
        else:
            raise ProcedimentoNaoEncontradoException(procedimento)
