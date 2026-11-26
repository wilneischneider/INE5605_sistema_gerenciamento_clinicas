from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from datetime import date as Date
from model.atendimento import Atendimento
from model.paciente import Paciente
from model.pessoa import Pessoa
from view.viewAtendimentos import ViewAtendimentos
from daos.daoAtendimentos import DaoAtendimentos


class ControllerAtendimento:
    def __init__(self, controller_sistema):
        self.__atendimentos_dao = DaoAtendimentos()
        self.__controller_sistema = controller_sistema
        self.__view_atendimento = ViewAtendimentos()

    def atendimentos(self) -> dict:
        return self.__atendimentos_dao.get_dict()

    def agendar_atendimento(self):
        controlador_clinica = self.__controller_sistema.controller_clinica
        controlador_paciente = self.__controller_sistema.controller_paciente
        controlador_tipo_atendimento = self.__controller_sistema.controller_tipo_de_atendimento
        controlador_pagamento = self.__controller_sistema.controller_pagamento
        clinicas = controlador_clinica.clinicas()
        cnpj = self.__view_atendimento.pegar_clinica(clinicas)
        if cnpj == None:
            self.abrir_tela()
        try:
            clinica = clinicas[cnpj]
        except KeyError:
            self.__view_atendimento.mostrar_mensagem("Clínica não encontrada!")
            self.abrir_tela()
        profissionais = clinica.profissionais
        if len(profissionais) == 0:
            self.__view_atendimento.mostrar_mensagem("Não há profissional associado à Clínica!")
            self.abrir_tela()
        cpf_profissional = self.__view_atendimento.pegar_profissional(profissionais)
        if cpf_profissional == None:
            self.abrir_tela()
        try:
            profissional = profissionais[cpf_profissional]
        except KeyError:
            self.__view_atendimento.mostrar_mensagem("Profissional não encontrado!")
            self.abrir_tela()
        tipos_atendimento = controlador_tipo_atendimento.listar_descricao_tipos_atendimento()
        tipo_selecionado = self.__view_atendimento.pegar_tipo_atendimento(tipos_atendimento)
        if tipo_selecionado == None:
            self.abrir_tela()
        elif tipo_selecionado not in tipos_atendimento:
            self.abrir_tela()
        else:
            tipo_de_atendimento = tipo_selecionado
        pacientes = controlador_paciente.pacientes()
        if len(pacientes) == 0:
            self.__view_atendimento.mostrar_mensagem("Nenhum paciente cadastrado!")
            self.abrir_tela()
        cpf_paciente = self.__view_atendimento.pegar_paciente(pacientes)
        if cpf_paciente == None:
            self.abrir_tela()
        try:
            paciente = pacientes[cpf_paciente]
        except KeyError:
            self.__view_atendimento.mostrar_mensagem("Paciente não encontrado!")
            self.abrir_tela()
        horario_atendimento = {'abre': clinica.horario_de_abertura,
                               'fecha': clinica.horario_de_fechamento}
        dados = self.__view_atendimento.pegar_dados_agendar_atendimento(horario_atendimento)
        if dados == None:
            self.abrir_tela()
        data = dados["data"]
        horario_inicio = dados["horario_inicio"]
        horario_fim = dados["horario_fim"]
        valor = dados["valor"]
        if (
                clinica.horario_de_abertura <= horario_inicio
                and clinica.horario_de_fechamento >= horario_fim
                and horario_fim > horario_inicio
        ):
            idade_paciente = self.calcular_idade_paciente_na_data_do_atendimento(paciente, data)
            if idade_paciente < 18:
                dados_responsavel = None
                while dados_responsavel == None:
                    dados_responsavel = self.__view_atendimento.pegar_dados_do_responsavel()
                    if dados_responsavel == None:
                        msg = 'Não é possível agendar atendimento para menores de 18 anos sem responsável!'
                        self.__view_atendimento.mostrar_mensagem(msg)
                try:
                    responsavel = Pessoa(dados_responsavel["nome"], dados_responsavel["celular"],
                                         dados_responsavel["cpf"])
                except TipoParametroIncorretoException as e:
                    self.__view_atendimento.mostrar_mensagem(e)
            for objeto in controlador_tipo_atendimento.tipos_de_atendimento():
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
                atendimentos = self.atendimentos()
                if cpf_paciente in atendimentos.keys():
                    if data in atendimentos[cpf_paciente].keys():
                        if horario_inicio in self.atendimentos[cpf_paciente][data].keys():
                            msg = "Erro! Já existe atendimento para este paciente no mesmo horário!"
                            self.__view_atendimento.mostrar_mensagem(msg)
                        else:
                            atendimentos_paciente = atendimentos[cpf_paciente]
                            atendimentos_paciente[cpf_paciente][data].update(
                                {horario_inicio: atendimento})
                            self.__atendimentos_dao.update(cpf_paciente, atendimentos_paciente)
                            self.__view_atendimento.mostrar_mensagem(
                                "Atendimento agendado com sucesso!")
                            controlador_pagamento.escolher_forma_pagamento()
                    else:
                        atendimentos_paciente = atendimentos[cpf_paciente]
                        atendimentos_paciente.update({data: {horario_inicio: atendimento}})
                        self.__atendimentos_dao.update(cpf_paciente, atendimentos_paciente)
                        self.__view_atendimento.mostrar_mensagem("Atendimento agendado com sucesso!")
                        controlador_pagamento.escolher_forma_pagamento()
                else:
                    self.__atendimentos_dao.add(cpf_paciente, {data: {horario_inicio: atendimento}})
                    self.__view_atendimento.mostrar_mensagem("Atendimento agendado com sucesso!")
                    controlador_pagamento.escolher_forma_pagamento()
            except TipoParametroIncorretoException as e:
                self.__view_atendimento.mostrar_mensagem(e)
        else:
            msg = (
                f'Não foi possível agendar!'
                f' Horário de funcionamento da clínica: {clinica.horario_de_abertura} às {clinica.horario_de_fechamento}'
            )
            self.__view_atendimento.mostrar_mensagem(msg)

    def excluir_atendimento(self):
        controlador_paciente = self.__controller_sistema.controller_paciente
        pacientes = controlador_paciente.pacientes()
        if len(pacientes) == 0:
            self.__view_atendimento.mostrar_mensagem("Nenhum paciente cadastrado!")
            self.abrir_tela()
        cpf_paciente = self.__view_atendimento.pegar_paciente(pacientes)
        if cpf_paciente == None:
            self.abrir_tela()
        atendimentos = self.atendimentos()
        try:
            datas_atendimentos_paciente = atendimentos[cpf_paciente]
        except KeyError:
            self.__view_atendimento.mostrar_mensagem("Não existe atendimento para este Paciente!")
            self.abrir_tela()
        data_atendimento = self.__view_atendimento.pegar_data_atendimento(list(datas_atendimentos_paciente.keys()))
        if data_atendimento == None:
            self.abrir_tela()
        horarios_de_atendimentos = datas_atendimentos_paciente[data_atendimento]
        horario_atendimento = self.__view_atendimento.pegar_horario_atendimento(list(horarios_de_atendimentos.keys()))
        if horario_atendimento == None:
            self.abrir_tela()
        horarios_de_atendimentos.pop(horario_atendimento)
        if len(horarios_de_atendimentos) == 0:
            datas_atendimentos_paciente.pop(data_atendimento)
            if len(datas_atendimentos_paciente) == 0:
                self.__atendimentos_dao.remove(cpf_paciente)
            else:
                self.__atendimentos_dao.update(cpf_paciente, datas_atendimentos_paciente)
        else:
            datas_atendimentos_paciente.update({data_atendimento: horarios_de_atendimentos})
            self.__atendimentos_dao.update(cpf_paciente, datas_atendimentos_paciente)
        self.__view_atendimento.mostrar_mensagem("Atendimento excluído com sucesso!")

    def adicionar_procedimento(self):
        controlador_procedimento = self.__controller_sistema.controller_procedimento
        controlador_paciente = self.__controller_sistema.controller_paciente
        pacientes = controlador_paciente.pacientes()
        if len(pacientes) == 0:
            self.__view_atendimento.mostrar_mensagem("Nenhum paciente cadastrado!")
            self.abrir_tela()
        cpf_paciente = self.__view_atendimento.pegar_paciente(pacientes)
        if cpf_paciente == None:
            self.abrir_tela()
        atendimentos = self.atendimentos()
        try:
            datas_atendimentos_paciente = atendimentos[cpf_paciente]
        except KeyError:
            self.__view_atendimento.mostrar_mensagem("Não existe atendimento para este Paciente!")
            self.abrir_tela()
        data_atendimento = self.__view_atendimento.pegar_data_atendimento(list(datas_atendimentos_paciente.keys()))
        if data_atendimento == None:
            self.abrir_tela()
        horarios_de_atendimentos = datas_atendimentos_paciente[data_atendimento]
        horario_atendimento = self.__view_atendimento.pegar_horario_atendimento(list(horarios_de_atendimentos.keys()))
        if horario_atendimento == None:
            self.abrir_tela()
        atendimento = horarios_de_atendimentos[horario_atendimento]
        procedimentos = controlador_procedimento.procedimentos()
        if len(procedimentos) == 0:
            self.__view_atendimento.mostrar_mensagem("Nenhum procedimento cadastrado!")
            self.abrir_tela()
        procedimento = self.__view_atendimento.pegar_procedimento(procedimentos)
        if procedimento == None:
            self.abrir_tela()
        try:
            atendimento.incluir_procedimento(procedimento)
        except TipoParametroIncorretoException as e:
            self.__view_atendimento.mostrar_mensagem(e)
        else:
            horarios_de_atendimentos.update({horario_atendimento: atendimento})
            datas_atendimentos_paciente.update({data_atendimento: horarios_de_atendimentos})
            self.__atendimentos_dao.update(cpf_paciente, datas_atendimentos_paciente)
            self.__view_atendimento.mostrar_mensagem("Procedimento incluído com sucesso!")

    def consultar_atendimento(self):
        controlador_paciente = self.__controller_sistema.controller_paciente
        pacientes = controlador_paciente.pacientes()
        if len(pacientes) == 0:
            self.__view_atendimento.mostrar_mensagem("Nenhum paciente cadastrado!")
            self.abrir_tela()
        cpf_paciente = self.__view_atendimento.pegar_paciente(pacientes)
        if cpf_paciente == None:
            self.abrir_tela()
        atendimentos = self.atendimentos()
        try:
            datas_atendimentos_paciente = atendimentos[cpf_paciente]
        except KeyError:
            self.__view_atendimento.mostrar_mensagem("Não existe atendimento para este Paciente!")
            self.abrir_tela()
        data_atendimento = self.__view_atendimento.pegar_data_atendimento(list(datas_atendimentos_paciente.keys()))
        if data_atendimento == None:
            self.abrir_tela()
        horarios_de_atendimentos = datas_atendimentos_paciente[data_atendimento]
        horario_atendimento = self.__view_atendimento.pegar_horario_atendimento(list(horarios_de_atendimentos.keys()))
        if horario_atendimento == None:
            self.abrir_tela()
        atendimento = horarios_de_atendimentos[horario_atendimento]
        procedimentos = []
        for procedimento in atendimento.procedimentos_realizados:
            descricao = procedimento.descricao
            custo = procedimento.custo
            profissional = procedimento.profissional.nome
            procedimentos.append({"descricao": descricao, "custo": custo, "profissional": profissional})
        if atendimento.responsavel == None:
            responsavel = None
        else:
            responsavel = atendimento.responsavel.nome
        dados_mostrar = {
            "clinica": atendimento.clinica.nome,
            "cidade": atendimento.clinica.cidade,
            "paciente": atendimento.paciente.nome,
            "profissional": atendimento.profissional.nome,
            "especialidade": atendimento.profissional.especialidade,
            "data": atendimento.data,
            "horario_inicio": atendimento.horario_inicio,
            "horario_fim": atendimento.horario_fim,
            "tipo_de_atendimento": atendimento.tipo_de_atendimento.tipo,
            "valor": atendimento.valor,
            "procedimentos_realizados": procedimentos,
            "responsavel": responsavel
        }
        self.__view_atendimento.mostrar_dados_da_consulta(dados_mostrar)
        self.abrir_tela()

    def extrair_atendimentos(self):
        atendimentos_geral = self.atendimentos() #{cpf_paciente:{data:{horario_inicio:atendimento}}}
        if len(atendimentos_geral) > 0:
            lista_datas = [] #[{data:{horario_inicio:atendimento}}, {data:{horario_inicio:atendimento}}]
            for valor in atendimentos_geral.values():
                lista_datas.append(valor)
            lista_horarios = []
            for data in lista_datas:
                lista_horarios.append(data.values())
            lista_atendimentos = []
            a = 0
            while a < len(lista_horarios):
                horario = list(lista_horarios[a])
                b = 0
                while b < len(horario):
                    atendimento = horario[b].values()
                    for registro in atendimento:
                        lista_atendimentos.append(registro)
                    b += 1
                a += 1
            return lista_atendimentos
        else:
            return []

    def listar_atendimentos(self):
        lista_atendimentos = self.extrair_atendimentos()
        if len(lista_atendimentos) > 0:
            dados = []
            for atendimento in lista_atendimentos:
                nome_clinica = atendimento.clinica.nome
                cnpj_clinica = atendimento.clinica.cnpj
                tipo_atendimento = atendimento.tipo_de_atendimento.tipo
                data_atendimento = atendimento.data
                hora_atendimento = atendimento.horario_inicio
                nome_profissional = atendimento.profissional.nome
                nome_paciente = atendimento.paciente.nome
                valor_atendimento = atendimento.valor
                registro = {"nome_clinica": nome_clinica, "cnpj_clinica": cnpj_clinica,
                            "tipo_atendimento": tipo_atendimento, "data_atendimento": data_atendimento,
                            "hora_atendimento": hora_atendimento, "nome_profissional": nome_profissional,
                            "nome_paciente": nome_paciente, "valor_atendimento": valor_atendimento}
                dados.append(registro)
            self.__view_atendimento.mostrar_lista_atendimentos(dados)
            self.abrir_tela()
        else:
            msg = f'Não há atendimento cadastrado!'
            self.__view_atendimento.mostrar_mensagem(msg)
            self.abrir_tela()

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

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.agendar_atendimento, 2: self.adicionar_procedimento,
                  3: self.consultar_atendimento, 4: self.excluir_atendimento, 5: self.listar_atendimentos}
        while True:
            opcoes[self.__view_atendimento.view_opcoes()]()
