class TipoParametroIncorretoException(Exception):
    def __init__(self, tipo_esperado: str):
        self.mensagem = f"Erro! Este atributo requer um parâmetro do tipo {tipo_esperado}."
        super().__init__(self.mensagem)