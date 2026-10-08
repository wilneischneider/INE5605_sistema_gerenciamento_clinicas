from Model import pessoa
from Model.profissional import Profissional
from Controller.cpfJaCadastradoException import CpfJaCadastradoException
from Controller.cpfNaoEncontradoException import CpfNaoEncontradoException


class ControllerProfissional:
    def __init__(self):
        self.__profissionais = {}

    def listar_profissionais_cadastrados(self):
        return self.__profissionais.values()

    def listar_cpfs_cadastrados(self):
        return self.__profissionais.keys()

    def retornar_profissional(self, cpf:str) -> Profissional:
        if cpf in self.listar_cpfs_cadastrados():
            return self.__profissionais[cpf]
        else:
            raise CpfNaoEncontradoException(cpf)

    def cadastrar_profissional(self, nome:str, celular: str, cpf:str, especialidade:str, registro_profissional:str):
        if cpf not in self.listar_cpfs_cadastrados():
            profissional = Profissional(nome, celular, cpf, especialidade, registro_profissional)
            self.__profissionais.update({cpf: profissional})
            return True
        else:
            raise CpfJaCadastradoException(cpf)

    def excluir_profissional(self, cpf):
        if cpf in self.listar_cpfs_cadastrados():
            self.__profissionais.pop(cpf)
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def atualizar_nome(self, nome:str, cpf:str):
        if cpf in self.listar_cpfs_cadastrados():
            self.__profissionais[cpf].nome = nome
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def atualizar_celular(self, celular:str, cpf:str):
        if cpf in self.listar_cpfs_cadastrados():
            self.__profissionais[cpf].celular = celular
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def atualizar_especialidade(self, especialidade:str, cpf:str):
        if cpf in self.listar_cpfs_cadastrados():
            self.__profissionais[cpf].especialidade = especialidade
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def atualizar_registro_profissional(self, registro_profissional:str, cpf:str):
        if cpf in self.listar_cpfs_cadastrados():
            self.__profissionais[cpf].registro_profissional = registro_profissional
            return True
        else:
            raise CpfNaoEncontradoException(cpf)

    def corrigir_cpf(self, cpf_correto:str, cpf_cadastrado:str):
        if cpf_correto not in self.listar_cpfs_cadastrados():
            if cpf_cadastrado in self.listar_cpfs_cadastrados():
                profissional = self.__profissionais[cpf_cadastrado]
                profissional.cpf = cpf_correto
                self.__profissionais.pop(cpf_cadastrado)
                self.__profissionais.update({cpf_correto: profissional})
                return True
            else:
                raise CpfNaoEncontradoException(cpf_cadastrado)
        else:
            raise CpfJaCadastradoException(cpf_correto)
