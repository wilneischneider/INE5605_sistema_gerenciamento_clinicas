class ViewSistema:
    def entra_opcao_valida(self, mensagem: str = '', opcoes_validas = None):
        while True:
            opcao_escolhida = input(mensagem)
            try:
                opcao = int(opcao_escolhida)
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("Opção inválida!")

    def view_opcoes(self):
        print("-------- SISTEMA DE GERENCIAMENTO DE CLÍNICAS ---------")
        print("Escolha sua opção:")
        print("1 - Gerenciar Atendimentos")
        print("2 - Gerenciar Pagamentos")
        print("3 - Gerenciar Pacientes")
        print("4 - Gerenciar Procedimentos")
        print("5 - Gerenciar Profissionais")
        print("6 - Gerenciar Clínicas")
        print("0 - Finalizar sistema")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6])
        return opcao
