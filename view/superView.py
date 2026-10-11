class SuperView:
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
