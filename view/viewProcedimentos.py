from view.superView import SuperView


class ViewProcedimentos(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE PROCEDIMENTOS ---------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Procedimento")
        print("2 - Buscar Procedimento")
        print("3 - Listar Procedimentos")
        print("4 - Excluir Procedimento")
        print("5 - Alterar Custo do Procedimento")
        print("6 - Alterar Profissional Responsável")
        print("7 - Corrigir Descrição")
        print("0 - Retornar")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6,7])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_descricao(self):
        descricao = input("Informe a descrição do Procedimento: ")
        return descricao

    def mostrar_dados_procedimento(self, lista_dados:list):
        print("--- PROCEDIMENTO(S) CADASTRADO(S) ---")
        if len(lista_dados) > 0:
            for dados_procedimento in lista_dados:
                print("Descrição: ", dados_procedimento["descricao"])
                print("Custo: ", dados_procedimento["custo"])
                print("Profissional: ", dados_procedimento["profissional"])
                print("--------------------------------")
        else:
            print("Nenhum procedimento encontrado!")

    def pegar_dados_procedimento(self):
        print("-------- CADASTRO DE PROCEDIMENTO ----------")
        descricao = input("Descrição: ")
        custo = input("Custo (informar apenas valor): ")
        cpf_profissional = input("CPF do Profissional Responsável: ")
        return {"descricao": descricao, "custo": custo, "cpf_profissional": cpf_profissional}

    def pegar_novo_custo(self):
        descricao = input("Informe a descrição do Procedimento: ")
        custo = input("Informe o novo custo: ")
        return {"descricao": descricao, "custo": custo}

    def pegar_novo_profissional(self):
        descricao = input("Informe a descrição do Procedimento: ")
        cpf_profissional = input("Informe o CPF do novo Profissional Responsável: ")
        return {"descricao": descricao, "cpf_profissional": cpf_profissional}

    def pegar_descricao_correta(self):
        descricao_correta = input("Informe a descrição correta do Procedimento: ")
        descricao_cadastrada = input("Informe a descrição cadastrada: ")
        return {"descricao_correta": descricao_correta, "descricao_cadastrada": descricao_cadastrada}
