from controller import controllerSistema
from model.paciente import Paciente
from exceptions.cpfJaCadastradoException import CpfJaCadastradoException
from exceptions.cpfNaoEncontradoException import CpfNaoEncontradoException
from datetime import date as Date
from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from view.viewPacientes import ViewPacientes
from controller import controllerSistema


class ControllerPaciente:
    def __init__(self, controller_sistema: controllerSistema):
        self.__pacientes = {}
        self.__controller_sistema = controller_sistema
        self.__view_pacientes = ViewPacientes()

    def listar_pacientes_cadastrados(self) -> list:
        return self.__pacientes.values()

    def listar_cpfs_cadastrados(self) -> list:
        return self.__pacientes.keys()

    def retornar_paciente(self, cpf:str) -> Paciente:
        if cpf in self.listar_cpfs_cadastrados():
            return self.__pacientes[cpf]
        else:
            raise CpfNaoEncontradoException(cpf)

    def cadastrar_paciente(self, nome:str, celular: str, cpf:str, data_de_nascimento: Date):
        if cpf not in self.listar_cpfs_cadastrados():
            try:
                paciente = Paciente(nome, celular, cpf, data_de_nascimento)
                self.__pacientes.update({cpf: paciente})
            except TipoParametroIncorretoException as e:
                print e ## VER COMO FAZER
                return 'Tipo de parâmetro incorreto'
        else:
            raise CpfJaCadastradoException(cpf)

    def excluir_paciente(self, cpf):
        if cpf in self.listar_cpfs_cadastrados():
            self.__pacientes.pop(cpf)
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def atualizar_nome(self, nome:str, cpf:str):
        if cpf in self.listar_cpfs_cadastrados():
            self.__pacientes[cpf].nome = nome
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def atualizar_celular(self, celular:str, cpf:str):
        if cpf in self.listar_cpfs_cadastrados():
            self.__pacientes[cpf].celular = celular
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def corrigir_data_de_nascimento(self, data_de_nascimento:Date, cpf:str):
        if cpf in self.listar_cpfs_cadastrados():
            self.__pacientes[cpf].data_de_nascimento = data_de_nascimento
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def corrigir_cpf(self, cpf_correto:str, cpf_cadastrado:str):
        if cpf_correto not in self.listar_cpfs_cadastrados():
            if cpf_cadastrado in self.listar_cpfs_cadastrados():
                paciente = self.__pacientes[cpf_cadastrado]
                paciente.cpf = cpf_correto
                self.__pacientes.pop(cpf_cadastrado)
                self.__pacientes.update({cpf_correto: paciente})
                return True
            else:
                raise CpfNaoEncontradoException(cpf_cadastrado)
        else:
            raise CpfJaCadastradoException(cpf_correto)

    def calcular_idade_paciente(self, cpf:str) -> int:#MOVIDO PARA O MODELO PACIENTE
        if cpf in self.listar_cpfs_cadastrados():
            paciente = self.__pacientes[cpf]
            data_de_nascimento = paciente.data_de_nascimento
            hoje = Date.today()
            if (
                hoje.month >= data_de_nascimento.month
                and hoje.day >= data_de_nascimento.day
            ):
                idade = hoje.year - data_de_nascimento.year
            else:
                idade = hoje.year - data_de_nascimento.year - 1
            return idade
        else:
            CpfNaoEncontradoException(cpf)
