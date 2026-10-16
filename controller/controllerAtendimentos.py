from os import supports_dir_fd

from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from datetime import date as Date
from model.atendimento import Atendimento
from model.clinica import Clinica
from model.paciente import Paciente
from model.pessoa import Pessoa
from view.viewAtendimentos import ViewAtendimentos


class ControllerAtendimento:
    def __init__(self, controller_sistema):
        self.__atendimentos = {} #{cpf_paciente:{data:{horario_inicio:atendimento}}}
        self.__controller_sistema = controller_sistema
        self.__view_atendimento = ViewAtendimentos()

    @property
    def atendimentos(self) -> dict:
        return self.__atendimentos

    def agendar_atendimento(self):
        controlador_clinica = self.__controller_sistema.controller_clinica
        controlador_paciente = self.__controller_sistema.controller_paciente
        controlador_tipo_atendimento = self.__controller_sistema.controller_tipo_de_atendimento
        controlador_pagamento = self.__controller_sistema.controller_pagamento
        dados = self.__view_atendimento.pegar_dados_agendar_atendimento()
        cnpj = dados["cnpj"]
        cpf_paciente = dados["cpf_paciente"]
        cpf_profissional = dados["cpf_profissional"]
        data = dados["data"]
        horario_inicio = dados["horario_inicio"]
        horario_fim = dados["horario_fim"]
        tipo_de_atendimento = dados["tipo_de_atendimento"]
        valor = dados["valor"]
        if cnpj in controlador_clinica.listar_cnpjs_cadastrados():
            clinica = controlador_clinica.clinicas[cnpj]
            if (
                clinica.horario_de_abertura <= horario_inicio
                and clinica.horario_de_fechamento >= horario_fim
                and horario_fim > horario_inicio
            ):
                if cpf_paciente in controlador_paciente.listar_cpfs_cadastrados():
                    profissionais_da_clinica = clinica.profissionais
                    if cpf_profissional in profissionais_da_clinica.keys():
                        if tipo_de_atendimento in controlador_tipo_atendimento.listar_descricao_tipos_atendimento():
                            paciente = controlador_paciente.pacientes[cpf_paciente]
                            idade_paciente = self.calcular_idade_paciente_na_data_do_atendimento(paciente, data)
                            if idade_paciente < 18:
                                dados_responsavel = self.__view_atendimento.pegar_dados_do_responsavel()
                                try:
                                    responsavel = Pessoa(dados_responsavel["nome"], dados_responsavel["celular"],
                                                         dados_responsavel["cpf"])
                                except TipoParametroIncorretoException as e:
                                    self.__view_atendimento.mostrar_mensagem(e)
                            profissional = profissionais_da_clinica[cpf_profissional]
                            for objeto in controlador_tipo_atendimento.tipos_de_atendimento:
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
                                if cpf_paciente in self.atendimentos.keys():
                                    if data in self.atendimentos[cpf_paciente].keys():
                                        if horario_inicio in self.atendimentos[cpf_paciente][data].keys():
                                            msg = "Erro! Já existe atendimento para este paciente no mesmo horário!"
                                            self.__view_atendimento.mostrar_mensagem(msg)
                                        else:
                                            self.__atendimentos[cpf_paciente][data].update(
                                                {horario_inicio: atendimento})
                                            self.__view_atendimento.mostrar_mensagem(
                                                "Atendimento agendado com sucesso!")
                                            controlador_pagamento.escolher_forma_pagamento()
                                    else:
                                        self.__atendimentos[cpf_paciente].update({data:{horario_inicio:atendimento}})
                                        self.__view_atendimento.mostrar_mensagem("Atendimento agendado com sucesso!")
                                        controlador_pagamento.escolher_forma_pagamento()
                                else:
                                    self.__atendimentos.update({cpf_paciente:{data:{horario_inicio:atendimento}}})
                                    self.__view_atendimento.mostrar_mensagem("Atendimento agendado com sucesso!")
                                    controlador_pagamento.escolher_forma_pagamento()
                            except TipoParametroIncorretoException as e:
                                self.__view_atendimento.mostrar_mensagem(e)
                        else:
                            msg = (
                                f'Tipo de atendimento "{tipo_de_atendimento}" não cadastrado!'
                                f' Tipos cadastrados: {controlador_tipo_atendimento.listar_descricao_tipos_atendimento()}'
                            )
                            self.__view_atendimento.mostrar_mensagem(msg)
                    else:
                        msg = f'Não há profissional de CPF "{cpf_profissional}" vinculado à clinica informada!'
                        self.__view_atendimento.mostrar_mensagem(msg)
                else:
                    self.__view_atendimento.mostrar_mensagem(f'Não há paciente de CPF "{cpf_paciente}" cadastrado!')
            else:
                msg = (
                    f'Não foi possível agendar!'
                    f' Horário de funcionamento da clínica: {clinica.horario_de_abertura} às {clinica.horario_de_fechamento}'
                )
                self.__view_atendimento.mostrar_mensagem(msg)
        else:
            self.__view_atendimento.mostrar_mensagem(f'Nenhuma clínica encontrada com o CNPJ "{cnpj}"')

    def excluir_atendimento(self):
        self.__view_atendimento.mostrar_mensagem("--- Excluir atendimento ---")
        dados = self.__view_atendimento.pegar_dados_da_consulta()
        try:
            datas_atendimentos_paciente = self.atendimentos[dados["cpf_paciente"]]
            horarios_de_atendimentos = datas_atendimentos_paciente[dados["data"]]
            horarios_de_atendimentos[dados["horario_inicio"]]
        except KeyError:
            msg = (f'Não há atendimento para o CPF "{dados["cpf_paciente"]}" em'
                   f' {dados["data"]}, às {dados["horario_inicio"]}.')
            self.__view_atendimento.mostrar_mensagem(msg)
        else:
            horarios_de_atendimentos.pop(dados["horario_inicio"])
            if len(horarios_de_atendimentos) == 0:
                datas_atendimentos_paciente.pop(dados["data"])
                if len(datas_atendimentos_paciente) == 0:
                    self.__atendimentos.pop(dados["cpf_paciente"])
                else:
                    self.__atendimentos.update({dados["cpf_paciente"]: datas_atendimentos_paciente})
            else:
                datas_atendimentos_paciente.update({dados["data"]: horarios_de_atendimentos})
                self.__atendimentos.update({dados["cpf_paciente"]: datas_atendimentos_paciente})
            self.__view_atendimento.mostrar_mensagem("Atendimento excluído com sucesso!")

    def adicionar_procedimento(self):
        controlador_procedimento = self.__controller_sistema.controller_procedimento
        dados = self.__view_atendimento.pegar_dados_procedimento_na_consulta()
        if dados["descricao_procedimento"] in controlador_procedimento.listar_descricao_procedimentos_cadastrados():
            procedimento = controlador_procedimento.procedimentos[dados["descricao_procedimento"]]
            try:
                datas_atendimentos_paciente = self.atendimentos[dados["cpf_paciente"]]
                horarios_de_atendimentos = datas_atendimentos_paciente[dados["data"]]
                atendimento = horarios_de_atendimentos[dados["horario_inicio"]]
            except KeyError:
                msg = (f'Não há atendimento para o CPF "{dados["cpf_paciente"]}" em'
                       f' {dados["data"]}, às {dados["horario_inicio"]}.')
                self.__view_atendimento.mostrar_mensagem(msg)
            else:
                try:
                    atendimento.incluir_procedimento(procedimento)
                except TipoParametroIncorretoException as e:
                    self.__view_atendimento.mostrar_mensagem(e)
                else:
                    horarios_de_atendimentos.update({dados["horario_inicio"]:atendimento})
                    datas_atendimentos_paciente.update({dados["data"]:horarios_de_atendimentos})
                    self.__atendimentos.update({dados["cpf_paciente"]:datas_atendimentos_paciente})
                    self.__view_atendimento.mostrar_mensagem("Procedimento incluído com sucesso!")
        else:
            msg = f'Não há procedimento cadastrado com a descrição "{dados["descricao_procedimento"]}"'
            self.__view_atendimento.mostrar_mensagem(msg)

    def consultar_atendimento(self):
        dados = self.__view_atendimento.pegar_dados_da_consulta()
        try:
            datas_atendimentos_paciente = self.atendimentos[dados["cpf_paciente"]]
            horarios_de_atendimentos = datas_atendimentos_paciente[dados["data"]]
            atendimento = horarios_de_atendimentos[dados["horario_inicio"]]
        except KeyError:
            msg = (f'Não há atendimento para o CPF "{dados["cpf_paciente"]}" em'
                   f' {dados["data"]}, às {dados["horario_inicio"]}.')
            self.__view_atendimento.mostrar_mensagem(msg)
        else:
            procedimentos = []
            for procedimento in atendimento.procedimentos_realizados:
                descricao = procedimento.descricao
                custo = procedimento.custo
                profissional = procedimento.profissional.nome
                procedimentos.append({"descricao": descricao, "custo": custo, "profissional": profissional})
            if atendimento.responsavel == None:
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
                    "responsavel": None
                }
                self.__view_atendimento.mostrar_dados_da_consulta(dados_mostrar)
            else:
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
                    "responsavel": atendimento.responsavel.nome
                }
                self.__view_atendimento.mostrar_dados_da_consulta(dados_mostrar)

    def extrair_atendimentos(self):
        atendimentos_geral = self.atendimentos #{cpf_paciente:{data:{horario_inicio:atendimento}}}
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
        else:
            msg = f'Não há atendimento cadastrado!'
            self.__view_atendimento.mostrar_mensagem(msg)

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
