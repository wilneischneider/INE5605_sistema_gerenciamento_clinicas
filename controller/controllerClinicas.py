from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from model.clinica import Clinica
from view.viewClinicas import ViewClinicas
from daos.daoClinicas import DaoClinicas


class ControllerClinica:
    def __init__(self, controller_sistema):
        self.__clinicas_dao = DaoClinicas()
        self.__controller_sistema = controller_sistema
        self.__view_clinica = ViewClinicas()

    def clinicas(self):
        return self.__clinicas_dao.get_dict()

    def listar_clinicas_cadastradas(self):
        clinicas = self.clinicas()
        self.__view_clinica.mostrar_clinicas(list(clinicas.values()))
        self.abrir_tela()

    def listar_cnpjs_cadastrados(self) -> list:
        clinicas = self.__clinicas_dao.get_dict()
        return list(clinicas.keys())

    def retornar_clinica(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        clinica = clinicas[cnpj]
        self.__view_clinica.mostrar_clinicas([clinica])
        self.abrir_tela()

    def cadastrar_clinica(self):
        dados_clinica = self.__view_clinica.pegar_dados_da_clinica()
        if dados_clinica == None:
            self.abrir_tela()
        if (
            len(dados_clinica["cnpj"]) == 0
                or len(dados_clinica["nome"]) == 0
                or len(dados_clinica["cidade"]) == 0
                or len(dados_clinica["descricao"]) == 0
        ):
            self.__view_clinica.mostrar_mensagem("Obrigatório o preenchimento de todos os campos!")
            self.abrir_tela()
        if dados_clinica["cnpj"] not in self.listar_cnpjs_cadastrados():
            try:
                clinica = Clinica(
                    dados_clinica["cnpj"],
                    dados_clinica["nome"],
                    dados_clinica["cidade"],
                    dados_clinica["descricao"],
                    dados_clinica["horario_de_abertura"],
                    dados_clinica["horario_de_fechamento"]
                )
                self.__clinicas_dao.add(clinica)
                self.__view_clinica.mostrar_mensagem("Clínica cadastrada com sucesso!")
            except TipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ {dados_clinica["cnpj"]} já está cadastrado!')

    def excluir_clinica(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__clinicas_dao.remove(cnpj)
            self.__view_clinica.mostrar_mensagem('Clínica excluída com sucesso!')
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def atualizar_nome_clinica(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        clinica = clinicas[cnpj]
        nome_atual = clinica.nome
        novo_nome = self.__view_clinica.pegar_novo_nome(nome_atual)
        if novo_nome == None:
            self.abrir_tela()
        if len(novo_nome) == 0:
            self.__view_clinica.mostrar_mensagem('Obrigatório preencher nome da clínica!')
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            try:
                clinica.nome = novo_nome
                self.__clinicas_dao.update(clinica)
                self.__view_clinica.mostrar_mensagem('Nome da Clínica atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def atualizar_cidade(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        clinica = clinicas[cnpj]
        cidade_atual = clinica.cidade
        nova_cidade = self.__view_clinica.pegar_nova_cidade(cidade_atual)
        if nova_cidade == None:
            self.abrir_tela()
        if len(nova_cidade) == 0:
            self.__view_clinica.mostrar_mensagem('Obrigatório preencher nome da cidade!')
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            try:
                clinica.cidade = nova_cidade
                self.__clinicas_dao.update(clinica)
                self.__view_clinica.mostrar_mensagem('Cidade da Clínica atualizada com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def atualizar_descricao(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        clinica = clinicas[cnpj]
        descricao_atual = clinica.descricao
        nova_descricao = self.__view_clinica.pegar_nova_descricao(descricao_atual)
        if nova_descricao == None:
            self.abrir_tela()
        if len(nova_descricao) == 0:
            self.__view_clinica.mostrar_mensagem('Obrigatório preencher descrição da clinica!')
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            try:
                clinica.descricao = nova_descricao
                self.__clinicas_dao.update(clinica)
                self.__view_clinica.mostrar_mensagem('Descrição da Clínica atualizada com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def corrigir_cnpj(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        clinica = clinicas[cnpj]
        cnpj_cadastrado = clinica.cnpj
        cnpj_correto = self.__view_clinica.pegar_cnpj_correto(cnpj_cadastrado)
        if cnpj_correto == None:
            self.abrir_tela()
        if len(cnpj_correto) == 0:
            self.__view_clinica.mostrar_mensagem('Obrigatório preencher o CNPJ da clinica!')
            self.abrir_tela()
        if cnpj_correto not in self.listar_cnpjs_cadastrados():
            if cnpj_cadastrado in self.listar_cnpjs_cadastrados():
                try:
                    clinica.cnpj = cnpj_correto
                    self.__clinicas_dao.remove(cnpj_cadastrado)
                    self.__clinicas_dao.add(clinica)
                    self.__view_clinica.mostrar_mensagem(f'CNPJ corrigido com sucesso!')
                except TipoParametroIncorretoException as e:
                    self.__view_clinica.mostrar_mensagem(e)
            else:
                self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj_cadastrado}" não foi encontrada!')
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{cnpj_correto}" já está cadastrado!')

    def atualizar_horario_abertura_da_clinica(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        clinica = clinicas[cnpj]
        horario_atual = clinica.horario_de_abertura
        novo_horario = self.__view_clinica.pegar_novo_horario_de_abertura(horario_atual)
        if novo_horario == None:
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            try:
                clinica.horario_de_abertura = novo_horario
                self.__clinicas_dao.update(clinica)
                self.__view_clinica.mostrar_mensagem(f'Horário de abertura atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def atualizar_horario_fechamento_da_clinica(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        clinica = clinicas[cnpj]
        horario_atual = clinica.horario_de_fechamento
        novo_horario = self.__view_clinica.pegar_novo_horario_de_fechamento(horario_atual)
        if novo_horario == None:
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            try:
                clinica.horario_de_fechamento = novo_horario
                self.__clinicas_dao.update(clinica)
                self.__view_clinica.mostrar_mensagem(f'Horário de fechamento atualizado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def listar_profissionais_da_clinica(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            clinica = clinicas[cnpj]
            profissionais = clinica.profissionais
            lista_profissionais = []
            for profissional in profissionais.values():
                registro = {
                    "nome": profissional.nome,
                    "cpf": profissional.cpf,
                    "celular": profissional.celular,
                    "especialidade": profissional.especialidade
                }
                lista_profissionais.append(registro)
            self.__view_clinica.mostrar_profissionais(lista_profissionais)
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def vincular_profissional_a_clinica(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        controlador_profissional = self.__controller_sistema.controller_profissional
        profissionais = controlador_profissional.profissionais()
        cpf = self.__view_clinica.pegar_cpf_vincular_desvincular(profissionais)
        if cpf == None:
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            clinica = clinicas[cnpj]
            profissionais_da_clinica = clinica.profissionais
            if cpf not in profissionais_da_clinica.keys():
                if cpf in controlador_profissional.listar_cpfs_cadastrados():
                    try:
                        clinica.vincular_profissional(profissionais[cpf])
                        self.__clinicas_dao.update(clinica)
                        self.__view_clinica.mostrar_mensagem(f'Profissional vinculado com sucesso!')
                    except TipoParametroIncorretoException as e:
                        self.__view_clinica.mostrar_mensagem(e)
                else:
                    self.__view_clinica.mostrar_mensagem(
                        f'O profissional de CPF "{cpf}" não está cadastrado! Cadastre-o primeiro.'
                    )
            else:
                self.__view_clinica.mostrar_mensagem(f'O profissional já é vinculado à clinica!')
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def desvincular_profissional_da_clinica(self):
        clinicas = self.clinicas()
        cnpj = self.__view_clinica.pegar_cnpj(clinicas)
        if cnpj == None:
            self.abrir_tela()
        clinica = clinicas[cnpj]
        profissionais = clinica.profissionais
        cpf = self.__view_clinica.pegar_cpf_vincular_desvincular(profissionais)
        if cpf == None:
            self.abrir_tela()
        if cnpj in self.listar_cnpjs_cadastrados():
            try:
                clinica.desvincular_profissional(cpf)
                self.__clinicas_dao.update(clinica)
                self.__view_clinica.mostrar_mensagem(f'Profissional desvinculado com sucesso!')
            except TipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'A clínica de CNPJ "{cnpj}" não foi encontrada!')

    def desvincular_profissional_das_clinicas(self, cnpj: str, cpf: str):
        if cnpj in self.listar_cnpjs_cadastrados():
            clinicas = self.__clinicas_dao.get_dict()
            clinica = clinicas[cnpj]
            profissionais_da_clinica = clinica.profissionais
            if cpf in profissionais_da_clinica.keys():
                try:
                    clinica.desvincular_profissional(cpf)
                    self.__clinicas_dao.update(clinica)
                    return f'Desvinculado também da Clínica de CNPJ "{cnpj}"'
                except TipoParametroIncorretoException as e:
                    return e
            else:
                return None
        else:
            return None

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
