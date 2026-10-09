class PacienteMenorDeIdadeException(Exception):
    def __init__(self):
        self.mensagem = "O paciente informado é menor de idade."
        super().__init__(self.mensagem)
