from controller.controllerTiposDeAtendimento import ControllerTipoDeAtendimento
from controller.controllerRelatorios import ControllerRelatorios
from controller.controllerClinicas import ControllerClinica
from controller.controllerAtendimentos import ControllerAtendimento
from controller.controllerPacientes import ControllerPaciente
from controller.controllerPagamentos import ControllerPagamento
from controller.controllerProcedimentos import ControllerProcedimento
from controller.controllerProfissionais import ControllerProfissional
from view.viewSistema import ViewSistema


class ControllerSistema:
    def __init__(self):
        self.__controller_atendimento = ControllerAtendimento(self)
        self.__controller_clinica = ControllerClinica(self)
        self.__controller_paciente = ControllerPaciente(self)
        self.__controller_pagamento = ControllerPagamento(self)
        self.__controller_procedimento = ControllerProcedimento(self)
        self.__controller_profissional = ControllerProfissional(self)
        self.__controller_relatorios = ControllerRelatorios(self)
        self.__controller_tipo_de_atendimento = ControllerTipoDeAtendimento(self)
        self.__view_sistema = ViewSistema()

    @property
    def controller_tipo_de_atendimento(self):
        return self.__controller_tipo_de_atendimento

    @property
    def controller_atendimento(self):
        return self.__controller_atendimento

    @property
    def controller_clinica(self):
        return self.__controller_clinica

    @property
    def controller_paciente(self):
        return self.__controller_paciente

    @property
    def controller_pagamento(self):
        return self.__controller_pagamento

    @property
    def controller_procedimento(self):
        return self.__controller_procedimento

    @property
    def controller_profissional(self):
        return self.__controller_profissional

    @property
    def controller_relatorios(self):
        return self.__controller_relatorios

    def gerenciar_atendimentos(self):
        self.__controller_atendimento.abrir_tela()

    def gerenciar_clinicas(self):
        self.__controller_clinica.abrir_tela()

    def gerenciar_pacientes(self):
        self.__controller_paciente.abrir_tela()

    def gerenciar_pagamentos(self):
        self.__controller_pagamento.abrir_tela()

    def gerenciar_procedimentos(self):
        self.__controller_procedimento.abrir_tela()

    def gerenciar_profissionais(self):
        self.__controller_profissional.abrir_tela()

    def gerenciar_tipos_de_atendimento(self):
        self.__controller_tipo_de_atendimento.abrir_tela()

    def emitir_relatorios(self):
        self.__relatorios.abrir_tela()

    def inicializar_sistema(self):
        self.abrir_tela()

    def abrir_tela(self):
        opcoes = {1: self.gerenciar_atendimentos, 2: self.gerenciar_pagamentos, 3: self.gerenciar_pacientes,
                  4: self.gerenciar_procedimentos, 5: self.gerenciar_profissionais, 6: self.gerenciar_clinicas,
                  7: self.gerenciar_tipos_de_atendimento, 8: self.emitir_relatorios, 0: self.encerrar_sistema}
        while True:
            opcao_escolhida = self.__view_sistema.view_opcoes()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()

    def encerrar_sistema(self):
        exit(0)
