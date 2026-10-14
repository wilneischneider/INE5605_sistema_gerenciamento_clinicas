from view.superView import SuperView


class ViewTiposDeAtendimento(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE TIPOS DE ATENDIMENTO ---------")
        print("Escolha sua opção:")
        print("1 - Listar Tipos de Atendimento")
        print("2 - Cadastrar Tipo de Atendimento")
        print("3 - Excluir Tipo de Atendimento")
        print("0 - Retornar ao Menu Anterior")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_tipos_atendimento(self, tipos):
        print("--- Tipos de Atendimento ---")
        if len(tipos) > 0:
            for tipo in tipos:
                print(tipo)
        else:
            print("Nenhum tipo de atendimento cadastrado!")

    def pegar_tipo_atendimento(self):
        tipo_atendimento = input("Informe o nome do tipo de atendimento: ")
        return tipo_atendimento
