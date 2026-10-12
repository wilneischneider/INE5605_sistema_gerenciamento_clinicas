from controller.controllerTiposDeAtendimento import ControllerTipoDeAtendimento
from controllerClinicas import ControllerClinica
from controllerPacientes import ControllerPaciente
from controllerProfissionais import ControllerProfissional
from datetime import date as Date
from datetime import time as Time
from model.atendimento import Atendimento
from exceptions.pacienteMenorDeIdadeException import PacienteMenorDeIdadeException
from model.paciente import Paciente
from model.pessoa import Pessoa
from model.tipoDeAtendimento import TipoDeAtendimento
from view.viewAtendimentos import ViewAtendimentos


class ControllerAtendimento:
    def __init__(self, controller_sistema: ControllerSistema):
        self.__atendimentos = {} #{cpf_paciente:{data:{horario_inicio:atendimento}}}
        self.__controller_sistema = controller_sistema
        self.__view_atendimento = ViewAtendimentos()

    @property
    def atendimentos(self) -> dict:
        return self.__atendimentos

    def agendar_atendimento(self):
        dados = self.__view_atendimento.pegar_dados_agendar_atendimento()
        cnpj = dados["cnpj"]
        cpf_paciente = dados["cpf_paciente"]
        cpf_profissional = dados["cpf_profissional"]
        data = dados["data"]
        horario_inicio = dados["horario_inicio"]
        horario_fim = dados["horario_fim"]
        tipo_de_atendimento = dados["tipo_de_atendimento"]
        valor = dados["valor"]
        if cnpj in ControllerClinica.listar_cnpjs_cadastrados():
            clinica = ControllerClinica.clinicas[cnpj]
            if (
                clinica.horario_de_abertura <= horario_inicio
                and clinica.horario_de_fechamento >= horario_fim
                and horario_fim > horario_inicio
            ):
                if cpf_paciente in ControllerPaciente.listar_cpfs_cadastrados():
                    if cpf_profissional in ControllerProfissional.listar_cpfs_cadastrados():
                        if tipo_de_atendimento in ControllerTipoDeAtendimento.listar_descricao_tipos_atendimento():
                            paciente = ControllerPaciente.pacientes[cpf_paciente]
                            idade_paciente = calcular_idade_paciente_na_data_do_atendimento(paciente, data)
                            if idade_paciente < 18:
                                dados_responsavel = self.__view_atendimento.pegar_dados_do_responsavel()
                                try:
                                    responsavel = Pessoa(dados_responsavel["nome"], dados_responsavel["celular"],
                                                         dados_responsavel["cpf"])
                                except TipoParametroIncorretoException as e:
                                    self.__view_atendimento.mostrar_mensagem(e)
                            profissional = ControllerProfissional.profissionais[cpf_profissional]
                            for objeto in ControllerTipoDeAtendimento.tipos_de_atendimento:
                                if objeto.tipo == tipo_de_atendimento:
                                    tipo_atendimento = objeto
                            try:
                                atendimento = Atendimento(
                                    clinica,
                                    paciente,
                                    profissional,
                                    data,
                                    horario_inicio,
                                    horario_fim,
                                    tipo_atendimento,
                                    valor
                                )
                                if idade_paciente < 18:
                                    atendimento.responsavel = responsavel
                                self.__atendimentos.update({cpf_paciente:{data:{horario_inicio:atendimento}}})
                                self.__view_atendimento.mostrar_mensagem("Atendimento agendado com sucesso!")
                            except TipoParametroIncorretoException as e:
                                self.__view_atendimento.mostrar_mensagem(e)
                        else:
                            msg = (
                                f'Tipo de atendimento "{tipo_de_atendimento}" não cadastrado!/n'
                                f'Tipos cadastrados: {ControllerTipoDeAtendimento.listar_descricao_tipos_atendimento()}'
                            )
                            self.__view_atendimento.mostrar_mensagem(msg)
                    else:
                        msg = f'Não há profissional de CPF "{cpf_profissional}" cadastrado!'
                        self.__view_atendimento.mostrar_mensagem(msg)
                else:
                    self.__view_atendimento.mostrar_mensagem(f'Não há paciente de CPF "{cpf_paciente}" cadastrado!')
            else:
                msg = (
                    f'Não foi possível agendar!/n'
                    f'Horário de funcionamento da clínica: {clinica.horario_de_abertura} às {clinica.horario_de_fechamento}'
                )
                self.__view_atendimento.mostrar_mensagem(msg)
        else:
            self.__view_atendimento.mostrar_mensagem(f'Nenhuma clínica encontrada com o CNPJ "{cnpj}"')

    def cancelar_atendimento(self): #implementar se der tempo
        pass


    #COPIADO PARA CÁ, PRECISA AJUSTAR O CODIGO
    def adicionar_procedimento(self, descricao:str):
        if descricao in ControllerProcedimento.listar_descricao_procedimentos_cadastrados():
            procedimento = ControllerProcedimento.retornar_procedimento(descricao)
            self.__procedimentos_realizados.append(procedimento)
        else:
            raise ProcedimentoNaoEncontradoException(procedimento)

    def calcular_idade_paciente_na_data_do_atendimento(
            self,
            paciente: Paciente,
            data_atendimento:Date
    ) -> int:
        data_de_nascimento = paciente.data_de_nascimento
        if (
                data_atendimento.month >= data_de_nascimento.month
                and data_atendimento.day >= data_de_nascimento.day
        ):
            idade = data_atendimento.year - data_de_nascimento.year
        else:
            idade = data_atendimento.year - data_de_nascimento.year - 1
        return idade
