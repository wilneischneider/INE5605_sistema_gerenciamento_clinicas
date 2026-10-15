from view.superView import SuperView


class ViewProfissionais(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE PROFISSIONAIS ---------")
        print("Escolha sua opção:")
        print("1 - Listar Profissionais")
        print("2 - Cadastrar Profissional")
        print("3 - Buscar Profissional")
        print("4 - Excluir Profissional")
        print("5 - Atualizar Nome do(a) Profissional")
        print("6 - Atualizar Celular do(a) Profissional")
        print("7 - Atualizar Especialidade do(a) Profissional")
        print("8 - Atualizar Registro Profissional")
        print("9 - Corrigir CPF do(a) Profissional")
        print("0 - Retornar")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6,7,8,9])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def pegar_cpf(self):
        cpf = input("Informe o CPF do(a) Profissional: ")
        return cpf

    def mostrar_dados_profissional(self, lista_dados):
        print("--- PROFISSIONAL(IS) CADASTRADO(S) ---")
        if len(lista_dados) > 0:
            for dados_profissional in lista_dados:
                print("Nome: ", dados_profissional["nome"])
                print("Celular: ", dados_profissional["celular"])
                print("CPF: ", dados_profissional["cpf"])
                print("Especialidade: ", dados_profissional["especialidade"])
                print("Registro Profissional: ", dados_profissional["registro_profissional"])
                print("--------------------------------")
        else:
            print("Nenhum profissional encontrado!")

    def pegar_dados_profissional(self):
        print("-------- CADASTRO DE PROFISSIONAL ----------")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        registro_profissional = input("Registro Profissional: ")
        return {"nome": nome, "celular": celular, "cpf": cpf, "especialidade": especialidade,
                "registro_profissional": registro_profissional}

    def pegar_novo_nome(self):
        cpf = input("Informe o CPF do(a) Profissional: ")
        nome = input("Informe o novo nome do(a) Profissional: ")
        return {"nome": nome, "cpf": cpf}

    def pegar_novo_celular(self):
        cpf = input("Informe o CPF do(a) Profissional: ")
        celular = input("Informe o novo celular do(a) Profissional: ")
        return {"celular": celular, "cpf": cpf}

    def pegar_nova_especialidade(self):
        cpf = input("Informe o CPF do(a) Profissional: ")
        especialidade = input("Informe a nova especialidade do(a) Profissional: ")
        return {"especialidade": especialidade, "cpf": cpf}

    def pegar_novo_registro_profissional(self):
        cpf = input("Informe o CPF do(a) Profissional: ")
        registro_profissional = input("Informe o novo registro profissional: ")
        return {"registro_profissional": registro_profissional, "cpf": cpf}

    def pegar_cpf_correto(self):
        cpf_correto = input("Informe o CPF correto do(a) Profissional: ")
        cpf_cadastrado = input("Informe o CPF cadastrado: ")
        return {"cpf_correto": cpf_correto, "cpf_cadastrado": cpf_cadastrado}
