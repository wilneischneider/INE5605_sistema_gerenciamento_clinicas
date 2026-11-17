from view.viewPagamentos import ViewPagamentos
from model.pagamentoDinheiro import PagamentoDinheiro
from model.pagamentoPix import PagamentoPix
from model.pagamentoCartao import PagamentoCartao
from daos.daoPagamentos import DaoPagamentos
from datetime import datetime


class ControllerPagamento:
    def __init__(self, controller_sistema):
        self.__pagamentos_dao = DaoPagamentos()
        self.__controller_sistema = controller_sistema
        self.__view_pagamento = ViewPagamentos()

    def pagamentos(self):
        return self.__pagamentos_dao.get_all()

    def escolher_forma_pagamento(self):
        self.abrir_tela_opcoes_pagamento()

    def pagamento_dinheiro(self):
        controlador_atendimento = self.__controller_sistema.controller_atendimento
        cpf_paciente = self.__view_pagamento.pegar_cpf_paciente()
        data_atendimento = self.__view_pagamento.pegar_data_da_consulta()
        horario_atendimento = self.__view_pagamento.pegar_horario_da_consulta()
        try:
            atendimentos = controlador_atendimento.atendimentos()
            datas_atendimentos = atendimentos[cpf_paciente]
            horarios_atendimentos = datas_atendimentos[data_atendimento]
            atendimento = horarios_atendimentos[horario_atendimento]
            msg = f'Data de vencimento: {data_atendimento}'
            self.__view_pagamento.mostrar_mensagem(msg)
        except KeyError:
            self.__view_pagamento.mostrar_mensagem("Não há atendimento para os dados informados!")
        else:
            data = self.__view_pagamento.pegar_data_de_pagamento()
            if data <= data_atendimento:
                paciente = atendimento.paciente
                valor_pago = self.__view_pagamento.pegar_valor_do_pagamento()
                parcelas = self.__view_pagamento.pegar_numero_parcelas()
                pagamento = PagamentoDinheiro(paciente, atendimento, data, valor_pago, parcelas)
                agora = datetime.now()
                agora_formatado = agora.strftime("%Y%m%d%H%M%S")
                chave = agora_formatado + "_" + paciente.cpf
                self.__pagamentos_dao.add(chave, pagamento)
                self.__view_pagamento.mostrar_mensagem("Pagamento realizado com sucesso!")
            else:
                self.__view_pagamento.mostrar_mensagem("Prazo vencido! Não foi possível pagar!")

    def pagamento_pix(self):
        controlador_atendimento = self.__controller_sistema.controller_atendimento
        cpf_paciente = self.__view_pagamento.pegar_cpf_paciente()
        data_atendimento = self.__view_pagamento.pegar_data_da_consulta()
        horario_atendimento = self.__view_pagamento.pegar_horario_da_consulta()
        try:
            atendimentos = controlador_atendimento.atendimentos()
            datas_atendimentos = atendimentos[cpf_paciente]
            horarios_atendimentos = datas_atendimentos[data_atendimento]
            atendimento = horarios_atendimentos[horario_atendimento]
            msg = f'Data de vencimento: {data_atendimento}'
            self.__view_pagamento.mostrar_mensagem(msg)
        except KeyError:
            self.__view_pagamento.mostrar_mensagem("Não há atendimento para os dados informados!")
        else:
            data = self.__view_pagamento.pegar_data_de_pagamento()
            if data <= data_atendimento:
                paciente = atendimento.paciente
                valor_pago = self.__view_pagamento.pegar_valor_do_pagamento()
                parcelas = self.__view_pagamento.pegar_numero_parcelas()
                cpf_pagador = self.__view_pagamento.pegar_cpf_pagador()
                pagamento = PagamentoPix(paciente, atendimento, data, valor_pago, cpf_pagador, parcelas)
                agora = datetime.now()
                agora_formatado = agora.strftime("%Y%m%d%H%M%S")
                chave = agora_formatado + "_" + paciente.cpf
                self.__pagamentos_dao.add(chave, pagamento)
                self.__view_pagamento.mostrar_mensagem("Pagamento realizado com sucesso!")
            else:
                self.__view_pagamento.mostrar_mensagem("Prazo vencido! Não foi possível pagar!")

    def pagamento_cartao(self):
        controlador_atendimento = self.__controller_sistema.controller_atendimento
        cpf_paciente = self.__view_pagamento.pegar_cpf_paciente()
        data_atendimento = self.__view_pagamento.pegar_data_da_consulta()
        horario_atendimento = self.__view_pagamento.pegar_horario_da_consulta()
        try:
            atendimentos = controlador_atendimento.atendimentos()
            datas_atendimentos = atendimentos[cpf_paciente]
            horarios_atendimentos = datas_atendimentos[data_atendimento]
            atendimento = horarios_atendimentos[horario_atendimento]
            msg = f'Data de vencimento: {data_atendimento}'
            self.__view_pagamento.mostrar_mensagem(msg)
        except KeyError:
            self.__view_pagamento.mostrar_mensagem("Não há atendimento para os dados informados!")
        else:
            data = self.__view_pagamento.pegar_data_de_pagamento()
            if data <= data_atendimento:
                paciente = atendimento.paciente
                valor_pago = self.__view_pagamento.pegar_valor_do_pagamento()
                parcelas = self.__view_pagamento.pegar_numero_parcelas()
                cpf_pagador = self.__view_pagamento.pegar_cpf_pagador()
                cartao = self.__view_pagamento.pegar_dados_do_cartao()
                cartao_numero = cartao["numero"]
                cartao_bandeira = cartao["bandeira"]
                pagamento = PagamentoCartao(paciente, atendimento, data, valor_pago, cpf_pagador,
                                            cartao_numero, cartao_bandeira, parcelas)
                agora = datetime.now()
                agora_formatado = agora.strftime("%Y%m%d%H%M%S")
                chave = agora_formatado + "_" + paciente.cpf
                self.__pagamentos_dao.add(chave, pagamento)
                self.__view_pagamento.mostrar_mensagem("Pagamento realizado com sucesso!")
            else:
                self.__view_pagamento.mostrar_mensagem("Prazo vencido! Não foi possível pagar!")

    def consultar_saldo_devedor(self):
        controlador_atendimento = self.__controller_sistema.controller_atendimento
        cpf_paciente = self.__view_pagamento.pegar_cpf_paciente()
        try:
            atendimentos = controlador_atendimento.atendimentos()
            datas_atendimentos = atendimentos[cpf_paciente] #{data:{horario_inicio:atendimento}, data:{horario_inicio:atendimento}}
            lista_datas_atendimentos = []
            valor_total = 0
            for data, horario_inicio in datas_atendimentos.items():
                for horario, atendimento in horario_inicio.items():
                    valor_atendimento = atendimento.valor
                    valor_procedimentos = 0
                    for procedimento in atendimento.procedimentos_realizados:
                        valor_procedimentos = valor_procedimentos + procedimento.custo
                    valor_total = valor_total + valor_atendimento + valor_procedimentos
                    valores = {"data": data, "horario": horario, "valor_atendimento": valor_atendimento,
                               "valor_procedimentos": valor_procedimentos}
                    lista_datas_atendimentos.append(valores)
            if len(lista_datas_atendimentos) > 0:
                pagamentos_realizados = 0
                for pagamento in self.pagamentos():
                    if pagamento.paciente.cpf == cpf_paciente:
                        pagamentos_realizados = pagamentos_realizados + pagamento.valor_pago
                saldo_devedor = valor_total - pagamentos_realizados
                dados = {"atendimentos": lista_datas_atendimentos, "total_pago": pagamentos_realizados,
                        "saldo": saldo_devedor}
                self.__view_pagamento.mostrar_valores_em_aberto(dados)
            else:
                self.__view_pagamento.mostrar_mensagem('Não há atendimento para os dados informados!')
        except KeyError:
            self.__view_pagamento.mostrar_mensagem('Não há atendimento para o CPF informado!')

    def consultar_pagamentos(self):
        cpf_paciente = self.__view_pagamento.pegar_cpf_paciente()
        pagamentos_paciente = []
        pagamentos = self.__pagamentos_dao.get_dict()
        for chave, registro in pagamentos.items():
            if registro.paciente.cpf == cpf_paciente:
                pagto = {"id": chave, "data": registro.data, "valor": registro.valor_pago}
                pagamentos_paciente.append(pagto)
        if len(pagamentos_paciente) > 0:
            self.__view_pagamento.mostrar_pagamentos_paciente(pagamentos_paciente)
        else:
            self.__view_pagamento.mostrar_mensagem('Não há pagamentos para o CPF informado!')

    def listar_pagamentos(self):
        pagamentos = []
        for registro in self.pagamentos():
            pagto = {"nome_paciente": registro.paciente.nome, "cpf_paciente": registro.paciente.cpf,
                     "data": registro.data, "valor": registro.valor_pago}
            pagamentos.append(pagto)
        if len(pagamentos) > 0:
            self.__view_pagamento.mostrar_pagamentos(pagamentos)
        else:
            self.__view_pagamento.mostrar_mensagem('Não há pagamentos registrados!')

    def excluir_pagamento(self):
        self.consultar_pagamentos()
        id_pagamento = self.__view_pagamento.pegar_id_pagamento()
        pagamentos = self.__pagamentos_dao.get_dict()
        if id_pagamento in pagamentos.keys():
            self.__pagamentos_dao.remove(id_pagamento)
            self.__view_pagamento.mostrar_mensagem('Pagamento excluido com sucesso!')
        else:
            self.__view_pagamento.mostrar_mensagem('Id incorreto! Pagamento não encontrado!')

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.escolher_forma_pagamento, 2: self.consultar_pagamentos,
                  3: self.listar_pagamentos, 4: self.consultar_saldo_devedor, 5: self.excluir_pagamento}
        while True:
            opcoes[self.__view_pagamento.view_opcoes()]()

    def abrir_tela_opcoes_pagamento(self):
        opcoes = {0: self.abrir_tela, 1: self.pagamento_dinheiro, 2: self.pagamento_pix,
                  3: self.pagamento_cartao}
        while True:
            opcoes[self.__view_pagamento.selecionar_forma_de_pagamento()]()
