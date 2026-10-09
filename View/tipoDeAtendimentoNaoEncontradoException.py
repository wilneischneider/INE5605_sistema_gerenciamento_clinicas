class TipoDeAtendimentoNaoEncontradoException(Exception):
    def __init__(self, descricao:str):
        self.mensagem = f"O tipo de atendimento '{descricao}' não foi encontrado."
        super().__init__(self.mensagem)
