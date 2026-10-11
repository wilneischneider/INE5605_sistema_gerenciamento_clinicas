from model.clinica import Clinica
from exceptions.cnpjJaCadastradoException import CnpjJaCadastradoException
from exceptions.cnpjNaoEncontradoException import CnpjNaoEncontradoException
from controller.controllerProfissionais import ControllerProfissional
from exceptions.profissionalNaoCadastradoException import ProfissionalNaoCadastradoException
from exceptions.cpfJaCadastradoException import CpfJaCadastradoException
from exceptions.cpfNaoEncontradoException import CpfNaoEncontradoException
from datetime import time as Time
from controller.controllerSistema import ControllerSistema
from view.viewClinicas import ViewClinicas


class ControllerClinica:
    def __init__(self, controller_sistema: ControllerSistema):
        self.__clinicas = {}
        self.__controller_sistema = controller_sistema
        self.__view_clinica = ViewClinicas()

    def listar_clinicas_cadastradas(self) -> list:
        return self.__clinicas.values()

    def listar_cnpjs_cadastrados(self) -> list:
        return self.__clinicas.keys()

    def retornar_clinica(self, cnpj) -> Clinica:
        if cnpj in self.listar_cnpjs_cadastrados():
            return self.__clinicas[cnpj]
        else:
            raise CnpjNaoEncontradoException(cnpj)

    def cadastrar_clinica(self, cnpj:str, nome:str, cidade: str, descricao:str):
        if cnpj not in self.listar_clinicas_cadastradas():
            clinica = Clinica(cnpj, nome, cidade, descricao)
            self.__clinicas.update({cnpj: clinica})
            return True
        else:
            raise CnpjJaCadastradoException(cnpj)

    def excluir_clinica(self, cnpj):
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__clinicas.pop(cnpj)
            return True
        else:
            raise CnpjNaoEncontradoException(cnpj)

    def atualizar_nome_clinica(self, nome:str, cnpj:str):
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__clinicas[cnpj].nome = nome
            return True
        else:
            raise CnpjNaoEncontradoException(cnpj)

    def atualizar_cidade(self, cidade:str, cnpj:str):
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__clinicas[cnpj].cidade = cidade
            return True
        else:
            raise CnpjNaoEncontradoException(cnpj)

    def atualizar_descricao(self, descricao:str, cnpj:str):
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__clinicas[cnpj].descricao = descricao
            return True
        else:
            raise CnpjNaoEncontradoException(cnpj)

    def corrigir_cnpj(self, cnpj_correto:str, cnpj_cadastrado:str):
        if cnpj_correto not in self.listar_cnpjs_cadastrados():
            if cnpj_cadastrado in self.listar_cnpjs_cadastrados():
                clinica = self.__clinicas[cnpj_cadastrado]
                clinica.cnpj = cnpj_correto
                self.__clinicas.pop(cnpj_cadastrado)
                self.__clinicas.update({cnpj_correto: clinica})
                return True
            else:
                raise CnpjNaoEncontradoException(cnpj_cadastrado)
        else:
            raise CnpjJaCadastradoException(cnpj_correto)

    def atualizar_horario_abertura_da_clinica(self, horario_abertura_da_clinica:Time, cnpj:str):
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__clinicas[cnpj].horario_de_abertura = horario_abertura_da_clinica
            return True
        else:
            raise CnpjNaoEncontradoException(cnpj)

    def atualizar_horario_fechamento_da_clinica(self, horario_fechamento_da_clinica: Time, cnpj: str):
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__clinicas[cnpj].horario_de_fechamento = horario_fechamento_da_clinica
            return True
        else:
            raise CnpjNaoEncontradoException(cnpj)

    def listar_profissionais_da_clinica(self, cnpj:str):
        if cnpj in self.listar_cnpjs_cadastrados():
            return self.retornar_clinica(cnpj).profissionais
        else:
            raise CnpjNaoEncontradoException(cnpj)

    def vincular_profissional_a_clinica(self, cnpj:str, cpf:str):
        clinica = self.retornar_clinica(cnpj)
        if cpf in ControllerProfissional.listar_cpfs_cadastrados():
            if cpf not in clinica.profissionais:
                clinica.vincular_profissional(cpf)
                self.__clinicas.update({cnpj:clinica})
            else:
                raise CpfJaCadastradoException(cpf)
        else:
            raise ProfissionalNaoCadastradoException(cpf)

    def desvincular_profissional_da_clinica(self, cnpj:str, cpf:str):
        clinica = self.retornar_clinica(cnpj)
        if cpf in clinica.profissionais:
            clinica.desvincular_profissional(cpf)
            self.__clinicas.update({cnpj: clinica})
        else:
            raise CpfNaoEncontradoException(cpf)

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.listar_clinicas_cadastradas, 2: self.cadastrar_clinica,
                  3: self.retornar_clinica, 4: self.excluir_clinica, 5: self.atualizar_nome_clinica,
                  6: self.atualizar_cidade, 7: self.atualizar_descricao, 8: self.corrigir_cnpj,
                  9: self.atualizar_horario_abertura_da_clinica, 10: self.atualizar_horario_fechamento_da_clinica,
                  11: self.listar_profissionais_da_clinica, 12: self.vincular_profissional_a_clinica,
                  13: self.desvincular_profissional_da_clinica}
        while True:
            opcoes[self.__view_clinica.view_opcoes()]()
