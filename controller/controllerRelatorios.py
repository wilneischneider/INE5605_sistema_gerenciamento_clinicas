# from controller.controllerAtendimentos import ControllerAtendimento
# from controller.controllerProcedimentos import ControllerProcedimento
from model.atendimento import Atendimento
from model.clinica import Clinica
from collections import Counter
from model.pessoa import Pessoa
from model.procedimento import Procedimento
from model.profissional import Profissional
from view.viewRelatorios import ViewRelatorios


class ControllerRelatorios:
    def __init__(self, controller_sistema):
        self.__controller_sistema = controller_sistema
        self.__view_relatorio = ViewRelatorios()

    def extrair_atendimentos(self):
        controlador_atendimento = self.__controller_sistema.controller_atendimento
        atendimentos_geral = controlador_atendimento.atendimentos #{cpf_paciente:{data:{horario_inicio:atendimento}}}
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

    def listar_clinicas_com_mais_atendimentos(self):
        lista_atendimentos = self.extrair_atendimentos()
        if len(lista_atendimentos) > 0:
            ocorrencias_clinicas = []
            for atendimento in lista_atendimentos:
                ocorrencias_clinicas.append(atendimento.clinica.cnpj)
            contagem_decrescente = dict(Counter(ocorrencias_clinicas).most_common()[:10])
            self.__view_relatorio.mostrar_clinicas_com_mais_atendimentos(contagem_decrescente)
        else:
            self.__view_relatorio.mostrar_mensagem("Nenhum atendimento encontrado!")

    def listar_atendimentos_mais_caros(self):
        lista_atendimentos = self.extrair_atendimentos()
        if len(lista_atendimentos) > 0:
            atendimentos_com_precos = {}
            for atendimento in lista_atendimentos:
                valor = atendimento.valor
                for procedimento in atendimento.procedimentos_realizados:
                    valor = valor + procedimento.custo
                atendimentos_com_precos.update({atendimento:valor})
            ordem_dec = dict(sorted(atendimentos_com_precos.items(), key=lambda item: item[1], reverse=True)[:10])
            resultado = []
            for chave, valor in ordem_dec.items():
                cnpj_clinica = chave.clinica.cnpj
                paciente = chave.paciente.nome
                profissional = chave.profissional.nome
                especialidade = chave.profissional.especialidade
                dicio = {"cnpj_clinica": cnpj_clinica, "nome_paciente": paciente, "nome_profissional": profissional,
                         "especialidade": especialidade, "valor": valor}
                resultado.append(dicio)
            self.__view_relatorio.mostrar_atendimentos_mais_caros(resultado)
        else:
            self.__view_relatorio.mostrar_mensagem("Nenhum atendimento encontrado!")

    def listar_atendimentos_mais_baratos(self):
        lista_atendimentos = self.extrair_atendimentos()
        if len(lista_atendimentos) > 0:
            atendimentos_com_precos = {}
            for atendimento in lista_atendimentos:
                valor = atendimento.valor
                for procedimento in atendimento.procedimentos_realizados:
                    valor = valor + procedimento.custo
                atendimentos_com_precos.update({atendimento: valor})
            ordem_cresc = dict(sorted(atendimentos_com_precos.items(), key=lambda item: item[1])[:10])
            resultado = []
            for chave, valor in ordem_cresc.items():
                cnpj_clinica = chave.clinica.cnpj
                paciente = chave.paciente.nome
                profissional = chave.profissional.nome
                especialidade = chave.profissional.especialidade
                dicio = {"cnpj_clinica": cnpj_clinica, "nome_paciente": paciente, "nome_profissional": profissional,
                         "especialidade": especialidade, "valor": valor}
                resultado.append(dicio)
            self.__view_relatorio.mostrar_atendimentos_mais_baratos(resultado)
        else:
            self.__view_relatorio.mostrar_mensagem("Nenhum atendimento encontrado!")

    def listar_procedimentos_mais_realizados(self):
        lista_atendimentos = self.extrair_atendimentos()
        if len(lista_atendimentos) > 0:
            ocorrencias_procedimentos = []
            for atendimento in lista_atendimentos:
                lista_procedimentos = atendimento.procedimentos_realizados
                for procedimento in lista_procedimentos:
                    ocorrencias_procedimentos.append(procedimento.descricao)
            contagem_decrescente = dict(Counter(ocorrencias_procedimentos).most_common()[:10])
            self.__view_relatorio.mostrar_procedimentos_mais_realizados(contagem_decrescente)
        else:
            self.__view_relatorio.mostrar_mensagem("Nenhum atendimento encontrado!")

    def listar_procedimentos_mais_caros(self):
        controlador_procedimento = self.__controller_sistema.controller_procedimento
        procedimentos = controlador_procedimento.procedimentos
        if len(procedimentos) > 0:
            procedimentos_com_custo = {}
            for procedimento in procedimentos.values():
                procedimentos_com_custo.update({procedimento:procedimento.custo})
            ordem_dec = dict(sorted(procedimentos_com_custo.items(), key=lambda item: item[1], reverse=True)[:10])
            resultado = []
            for chave, valor in ordem_dec.items():
                descricao = chave.descricao
                profissional = chave.profissional.nome
                especialidade = chave.profissional.especialidade
                dicio = {"descricao": descricao, "nome_profissional": profissional,
                         "especialidade": especialidade, "valor": valor}
                resultado.append(dicio)
            self.__view_relatorio.mostrar_procedimentos_mais_caros(resultado)
        else:
            self.__view_relatorio.mostrar_mensagem("Nenhum procedimento encontrado!")

    def listar_procedimentos_mais_baratos(self):
        controlador_procedimento = self.__controller_sistema.controller_procedimento
        procedimentos = controlador_procedimento.procedimentos
        if len(procedimentos) > 0:
            procedimentos_com_custo = {}
            for procedimento in procedimentos.values():
                procedimentos_com_custo.update({procedimento: procedimento.custo})
            ordem_cresc = dict(sorted(procedimentos_com_custo.items(), key=lambda item: item[1])[:10])
            resultado = []
            for chave, valor in ordem_cresc.items():
                descricao = chave.descricao
                profissional = chave.profissional.nome
                especialidade = chave.profissional.especialidade
                dicio = {"descricao": descricao, "nome_profissional": profissional,
                         "especialidade": especialidade, "valor": valor}
                resultado.append(dicio)
            self.__view_relatorio.mostrar_procedimentos_mais_baratos(resultado)
        else:
            self.__view_relatorio.mostrar_mensagem("Nenhum procedimento encontrado!")

    def retornar(self):
        self.__controller_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {0: self.retornar, 1: self.listar_clinicas_com_mais_atendimentos,
                  2: self.listar_atendimentos_mais_caros, 3: self.listar_atendimentos_mais_baratos,
                  4: self.listar_procedimentos_mais_realizados, 5: self.listar_procedimentos_mais_caros,
                  6:self.listar_procedimentos_mais_baratos}
        while True:
            opcoes[self.__view_relatorio.view_opcoes()]()
