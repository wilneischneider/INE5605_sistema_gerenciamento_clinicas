class ProfissionalNaoCadastradoException(Exception):
    def __init__(self, cpf: str):
        self.mensagem = f"CPF {cpf} não encontrado. Cadastre primeiro o profissional para depois vinculá-lo à clínica."
        super().__init__(self.mensagem)
