from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException
from model.clinica import Clinica
from controller.controllerProfissionais import ControllerProfissional
from controller.controllerSistema import ControllerSistema
from view.viewClinicas import ViewClinicas


class ControllerClinica:
    def __init__(self, controller_sistema: ControllerSistema):
        self.__clinicas = {}
        self.__controller_sistema = controller_sistema
        self.__view_clinica = ViewClinicas()

    @property
    def clinicas(self):
        return self.__clinicas

    def listar_clinicas_cadastradas(self):
        self.__view_clinica.mostrar_mensagem("--- Lista de Clínicas Cadastradas ---")
        for clinica in self.__clinicas.values():
            self.__view_clinica.mostrar_mensagem(f'Nome: {clinica.nome}')
            self.__view_clinica.mostrar_mensagem(f'CNPJ: {clinica.cnpj}')
            self.__view_clinica.mostrar_mensagem(f'Cidade: {clinica.cidade}')
            self.__view_clinica.mostrar_mensagem(f'Descrição: {clinica.descricao}')
            self.__view_clinica.mostrar_mensagem(
                f'Horário de Funcionamento: {clinica.horario_de_abertura} às {clinica.horario_de_fechamento}'
            )
            self.__view_clinica.mostrar_mensagem('--------------------------------------')

    def listar_cnpjs_cadastrados(self) -> list:
        return self.__clinicas.keys()

    def retornar_clinica(self):
        self.__view_clinica.mostrar_mensagem('--- Buscar Clínica ---')
        cnpj = self.__view_clinica.pegar_cnpj()
        if cnpj in self.listar_cnpjs_cadastrados():
            clinica = self.__clinicas[cnpj]
            self.__view_clinica.mostrar_mensagem(f'Nome: {clinica.nome}')
            self.__view_clinica.mostrar_mensagem(f'CNPJ: {clinica.cnpj}')
            self.__view_clinica.mostrar_mensagem(f'Cidade: {clinica.cidade}')
            self.__view_clinica.mostrar_mensagem(f'Descrição: {clinica.descricao}')
            self.__view_clinica.mostrar_mensagem(
                f'Horário de Funcionamento: {clinica.horario_de_abertura} às {clinica.horario_de_fechamento}'
            )
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{cnpj}" não foi encontrado!')

    def cadastrar_clinica(self):
        dados_clinica = self.__view_clinica.pegar_dados_da_clinica()
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
                self.__clinicas.update({dados_clinica["cnpj"]: clinica})
                self.__view_clinica.mostrar_mensagem("Clínica cadastrada com sucesso!")
            except TipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ {dados_clinica["cnpj"]} já está cadastrado!')

    def excluir_clinica(self, cnpj):
        self.__view_clinica.mostrar_mensagem('--- Excluir Clínica ---')
        cnpj = self.__view_clinica.pegar_cnpj()
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__clinicas.pop(cnpj)
            self.__view_clinica.mostrar_mensagem('Clínica excluída com sucesso!')
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{cnpj}" não foi encontrado!')

    def atualizar_nome_clinica(self):
        dados = self.__view_clinica.pegar_novo_nome()
        if dados["cnpj"] in self.listar_cnpjs_cadastrados():
            try:
                clinica = self.__clinicas[dados["cnpj"]]
                clinica.nome = dados["nome"]
                self.__clinicas.update({dados_clinica["cnpj"]: clinica})
                self.__view_clinica.mostrar_mensagem('Nome da Clínica atualizado com sucesso!')
            except tipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj"]}" não foi encontrado!')

    def atualizar_cidade(self):
        dados = self.__view_clinica.pegar_nova_cidade()
        if dados["cnpj"] in self.listar_cnpjs_cadastrados():
            try:
                clinica = self.__clinicas[dados["cnpj"]]
                clinica.cidade = dados["cidade"]
                self.__clinicas.update({dados_clinica["cnpj"]: clinica})
                self.__view_clinica.mostrar_mensagem('Cidade da Clínica atualizada com sucesso!')
            except tipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj"]}" não foi encontrado!')

    def atualizar_descricao(self):
        dados = self.__view_clinica.pegar_nova_descricao()
        if dados["cnpj"] in self.listar_cnpjs_cadastrados():
            try:
                clinica = self.__clinicas[dados["cnpj"]]
                clinica.descricao = dados["descricao"]
                self.__clinicas.update({dados_clinica["cnpj"]: clinica})
                self.__view_clinica.mostrar_mensagem('Descrição da Clínica atualizada com sucesso!')
            except tipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj"]}" não foi encontrado!')

    def corrigir_cnpj(self):
        dados = self.__view_clinica.pegar_cnpj_correto()
        if dados["cnpj_correto"] not in self.listar_cnpjs_cadastrados():
            if dados["cnpj_cadastrado"] in self.listar_cnpjs_cadastrados():
                try:
                    clinica = self.__clinicas[dados["cnpj_cadastrado"]]
                    clinica.cnpj = dados["cnpj_correto"]
                    self.__clinicas.pop(dados["cnpj_cadastrado"])
                    self.__clinicas.update({dados["cnpj_correto"]: clinica})
                    self.__view_clinica.mostrar_mensagem(f'CNPJ corrigido com sucesso!')
                except tipoParametroIncorretoException as e:
                    self.__view_clinica.mostrar_mensagem(e)
            else:
                self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj_cadastrado"]}" não foi encontrado!')
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj_correto"]}" já está cadastrado!')

    def atualizar_horario_abertura_da_clinica(self):
        dados = self.__view_clinica.pegar_novo_horario_de_abertura()
        if dados["cnpj"] in self.listar_cnpjs_cadastrados():
            try:
                clinica = self.__clinicas[dados["cnpj"]]
                clinica.horario_de_abertura = dados["horario_de_abertura"]
                self.__clinicas.update({dados["cnpj"]: clinica})
                self.__view_clinica.mostrar_mensagem(f'Horário de abertura atualizado com sucesso!')
            except tipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj"]}" não foi encontrado!')

    def atualizar_horario_fechamento_da_clinica(self):
        dados = self.__view_clinica.pegar_novo_horario_de_fechamento()
        if dados["cnpj"] in self.listar_cnpjs_cadastrados():
            try:
                clinica = self.__clinicas[dados["cnpj"]]
                clinica.horario_de_fechamento = dados["horario_de_fechamento"]
                self.__clinicas.update({dados["cnpj"]: clinica})
                self.__view_clinica.mostrar_mensagem(f'Horário de fechamento atualizado com sucesso!')
            except tipoParametroIncorretoException as e:
                self.__view_clinica.mostrar_mensagem(e)
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj"]}" não foi encontrado!')

    def listar_profissionais_da_clinica(self):
        cnpj = self.__view_clinica.pegar_cnpj()
        if cnpj in self.listar_cnpjs_cadastrados():
            self.__view_clinica.mostrar_mensagem('--- Lista de profissionais da Clínica ---')
            clinica = self.__clinicas[cnpj]
            profissionais = clinica.profissionais
            for profissional in profissionais.values():
                self.__view_clinica.mostrar_mensagem(f'Nome: {profissional.nome}')
                self.__view_clinica.mostrar_mensagem(f'CPF: {profissional.cpf}')
                self.__view_clinica.mostrar_mensagem(f'Celular: {profissional.celular}')
                self.__view_clinica.mostrar_mensagem(f'Especialidade: {profissional.especialidade}')
                self.__view_clinica.mostrar_mensagem('----------------------------------------------')
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{cnpj}" não foi encontrado!')

    def vincular_profissional_a_clinica(self):
        dados = self.__view_clinica.pegar_cpf_vincular_desvincular()
        if dados["cnpj"] in self.listar_cnpjs_cadastrados():
            clinica = self.__clinicas[dados["cnpj"]]
            profissionais_da_clinica = clinica.profissionais
            if dados["cpf"] not in profissionais_da_clinica.keys():
                if dados["cpf"] in ControllerProfissional.listar_cpfs_cadastrados():
                    try:
                        clinica.vincular_profissional(ControllerProfissional.profissionais[dados["cpf"]])
                        self.__clinicas.update({dados["cnpj"]: clinica})
                        self.__view_clinica.mostrar_mensagem(f'Profissional vinculado com sucesso!')
                    except tipoParametroIncorretoException as e:
                        self.__view_clinica.mostrar_mensagem(e)
                else:
                    self.__view_clinica.mostrar_mensagem(
                        f'O profissional de CPF "{dados["cpf"]}" não está cadastrado! Cadastre-o primeiro.'
                    )
            else:
                self.__view_clinica.mostrar_mensagem(f'O profissional já é vinculado à clinica!')
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj"]}" não foi encontrado!')

    def desvincular_profissional_da_clinica(self):
        dados = self.__view_clinica.pegar_cpf_vincular_desvincular()
        if dados["cnpj"] in self.listar_cnpjs_cadastrados():
            clinica = self.__clinicas[dados["cnpj"]]
            profissionais_da_clinica = clinica.profissionais
            if dados["cpf"] in profissionais_da_clinica.keys():
                try:
                    clinica.desvincular_profissional(dados["cpf"])
                    self.__clinicas.update({dados["cnpj"]: clinica})
                    self.__view_clinica.mostrar_mensagem(f'Profissional desvinculado com sucesso!')
                except tipoParametroIncorretoException as e:
                    self.__view_clinica.mostrar_mensagem(e)
            else:
                self.__view_clinica.mostrar_mensagem(
                    f'Não há profissional com o CPF "{dados["cpf"]}" vinculado à clínica!'
                )
        else:
            self.__view_clinica.mostrar_mensagem(f'O CNPJ "{dados["cnpj"]}" não foi encontrado!')

    def desvincular_profissional_das_clinicas(self, cnpj: str, cpf: str):
        if cnpj in self.listar_cnpjs_cadastrados():
            clinica = self.__clinicas[cnpj]
            profissionais_da_clinica = clinica.profissionais
            if cpf in profissionais_da_clinica.keys():
                try:
                    clinica.desvincular_profissional(cpf)
                    self.__clinicas.update({cnpj: clinica})
                    return f'Desvinculado também da Clínica de CNPJ "{cnpj}"'
                except tipoParametroIncorretoException as e:
                    return e
            else:
                return ''
        else:
            return ''

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
