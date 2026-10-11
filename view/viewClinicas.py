from view import superView


class ViewClinicas(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE CLÍNICAS ---------")
        print("Escolha sua opção:")
        print("1 - Listar Clínicas")
        print("2 - Cadastrar Clínica")
        print("3 - Buscar Clínica")
        print("4 - Excluir Clínica")
        print("5 - Atualizar Nome de Clínica")
        print("6 - Atualizar Cidade de Clínica")
        print("7 - Atualizar Descrição de Clínica")
        print("8 - Corrigir CNPJ de Clínica")
        print("9 - Atualizar Horário de Abertura de Clínica")
        print("10 - Atualizar Horário de Fechamento de Clínica")
        print("11 - Listar Profissionais de Clínica")
        print("12 - Vincular Profissional à Clínica")
        print("13 - Desvincular Profissional de Clínica")
        print("0 - Retornar ao Menu Anterior")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6,7,8,9,10,11,12,13])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_dados_da_clinica(self):
        print("-------- CADASTRO DE CLÍNICA ----------")
        nome = input("Nome: ")
        cnpj = input("CNPJ: ")
        cidade = input("Cidade: ")
        descricao = input("Descrição: ")
        return {"nome": nome, "cnpj": cnpj, "cidade": cidade, "descricao": descricao}
