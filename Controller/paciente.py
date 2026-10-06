from Model import pessoa
from Model.paciente import Paciente
from Controller.cpfJaCadastradoException import CpfJaCadastradoException
from Controller.cpfNaoEncontradoException import CpfNaoEncontradoException
from datetime import date as Date
from Model.pessoa import Pessoa


class ControllerPaciente(Paciente):
    def __init__(self):
        self.__pacientes = {}

    def listar_pacientes_cadastrados(self):
        return self.__pacientes.values()

    def listar_cpfs_cadastrados(self):
        return self.__pacientes.keys()

    def cadastrar_paciente(self, nome:str, celular: str, cpf:str, data_de_nascimento: Date):
        if cpf not in self.listar_cpfs_cadastrados():
            paciente = Paciente(nome, celular, cpf, data_de_nascimento)
            self.__pacientes.update({cpf: paciente})
            return True
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

    def atualizar_data_de_nascimento(self, data_de_nascimento:Date, cpf:str):
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
