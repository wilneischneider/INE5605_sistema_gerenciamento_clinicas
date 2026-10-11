from controller import controllerClinicas, controllerAtendimentos, controllerPacientes, controllerPagamentos, \
    controllerProcedimentos, controllerProfissionais, relatorios


class ControllerSistema:
    def __init__(self):
        self.__controller_atendimentos = controllerAtendimentos(self)
        self.__controller_clinicas = controllerClinicas(self)
        self.__controller_pacientes = controllerPacientes(self)
        self.__controller_pagamentos = controllerPagamentos(self)
        self.__controller_procedimentos = controllerProcedimentos(self)
        self.__controller_profissionais = controllerProfissionais(self)
        self.__relatorios = relatorios(self)
        self.__tela_sistema = ViewSistema()

    @property
    def controlador_amigos(self):
        return self.__controlador_amigos

    @property
    def controlador_livros(self):
        return self.__controlador_livros

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_livros(self):
        self.__controlador_livros.abre_tela()

    def cadastra_amigos(self):
        # Chama o controlador de Amigos
        self.__controlador_amigos.abre_tela()

    def cadastra_emprestimos(self):
        self.__controlador_emprestimos.abre_tela()
        # Chama o controlador de Emprestimos

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_livros, 2: self.cadastra_amigos, 3: self.cadastra_emprestimos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()