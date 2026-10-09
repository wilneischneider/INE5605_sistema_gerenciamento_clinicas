class TipoDeAtendimentoJaCadastradoException(Exception):
    def __init__(self, descricao:str):
        self.mensagem = f"O tipo de atendimento '{descricao}' já está cadastrado."
        super().__init__(self.mensagem)
