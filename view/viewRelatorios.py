from view.superView import SuperView


class ViewRelatorios(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE EMISSÃO DE RELATORIOS ---------")
        print("Escolha sua opção:")
        print("1 - Clínicas com maior número de atendimentos")
        print("2 - Atendimentos mais caros")
        print("3 - Atendimentos mais baratos")
        print("4 - Procedimentos mais realizados")
        print("5 - Procedimentos mais caros")
        print("6 - Procedimentos mais baratos")
        print("0 - Finalizar sistema")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_clinicas_com_mais_atendimentos(self, dados):
        print("--- 10 Clínicas com Maior Número de Atendimentos ---")
        for chave, valor in dados.items():
            print(f'CNPJ: {chave}, Número de Atendimentos: {valor}')
        print("---------------- Fim do Relatório ----------------")

    def mostrar_atendimentos_mais_caros(self, dados):
        print("--- 10 Atendimentos Mais Caros ---")
        for registro in dados:
            print(f'Clínica: {registro["cnpj_clinica"]}, Paciente: {registro["nome_paciente"]},'
                  f'Profissional: {registro["nome_profissional"]}, Especialidade: {registro["especialidade"]},'
                  f'Valor: {registro["valor"]}')
        print("---------------- Fim do Relatório ----------------")

    def mostrar_atendimentos_mais_baratos(self, dados):
        print("--- 10 Atendimentos Mais Baratos ---")
        for registro in dados:
            print(f'Clínica: {registro["cnpj_clinica"]}, Paciente: {registro["nome_paciente"]},'
                  f'Profissional: {registro["nome_profissional"]}, Especialidade: {registro["especialidade"]},'
                  f'Valor: {registro["valor"]}')
        print("---------------- Fim do Relatório ----------------")

    def mostrar_procedimentos_mais_realizados(self, dados):
        print("--- 10 Procedimentos Mais Realizados ---")
        for chave, valor in dados.items():
            print(f'Descrição: {chave}, Frequência: {valor}')
        print("---------------- Fim do Relatório ----------------")

    def mostrar_procedimentos_mais_caros(self, dados):
        print("--- 10 Procedimentos Mais Caros ---")
        for registro in dados:
            print(f'Descrição: {registro["descricao"]}, Profissional: {registro["nome_profissional"]},'
                  f' Especialidade: {registro["especialidade"]}, Valor: {registro["valor"]}')
        print("---------------- Fim do Relatório ----------------")

    def mostrar_procedimentos_mais_baratos(self, dados):
        print("--- 10 Procedimentos Mais Baratos ---")
        for registro in dados:
            print(f'Descrição: {registro["descricao"]}, Profissional: {registro["nome_profissional"]},'
                  f' Especialidade: {registro["especialidade"]}, Valor: {registro["valor"]}')
        print("---------------- Fim do Relatório ----------------")
