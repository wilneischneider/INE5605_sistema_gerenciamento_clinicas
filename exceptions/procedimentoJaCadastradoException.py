class ProcedimentoJaCadastradoException(Exception):
    def __init__(self, procedimento):
        self.mensagem = f"O procedimento {procedimento} já está cadastrado."
        super().__init__(self.mensagem)
