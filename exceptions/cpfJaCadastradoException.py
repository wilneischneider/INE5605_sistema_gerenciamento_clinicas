class CpfJaCadastradoException(Exception):
    def __init__(self, cpf):
        self.mensagem = f"O CPF {cpf} já está cadastrado."
        super().__init__(self.mensagem)
