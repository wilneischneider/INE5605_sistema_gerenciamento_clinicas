class CpfNaoEncontradoException(Exception):
    def __init__(self, cpf):
        self.mensagem = f"O CPF {cpf} não foi encontrado."
        super().__init__(self.mensagem)
