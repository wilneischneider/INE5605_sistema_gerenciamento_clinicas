class CnpjNaoEncontradoException(Exception):
    def __init__(self, cnpj):
        self.mensagem = f"O CNPJ {cnpj} não foi encontrado."
        super().__init__(self.mensagem)
