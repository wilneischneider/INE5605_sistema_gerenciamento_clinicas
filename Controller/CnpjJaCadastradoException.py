class CnpjJaCadastradoException(Exception):
    def __init__(self, cnpj):
        self.mensagem = f"O CNPJ {cnpj} já está cadastrado."
        super().__init__(self.mensagem)
