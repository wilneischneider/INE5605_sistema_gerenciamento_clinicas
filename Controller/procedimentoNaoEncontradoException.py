class ProcedimentoNaoEncontradoException(Exception):
    def __init__(self, procedimento):
        self.mensagem = f"O procedimento {procedimento} não foi encontrado."
        super().__init__(self.mensagem)
