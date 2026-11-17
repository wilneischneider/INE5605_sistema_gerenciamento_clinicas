from daos.dao import DAO
from model.abstractPagamento import AbstractPagamento


class DaoPagamentos(DAO):
    def __init__(self):
        super().__init__("pagamentos.pkl")

    def add(self, chave:str, pagamento: AbstractPagamento):
        if (
            pagamento is not None
            and isinstance(pagamento, AbstractPagamento)
            and isinstance(chave, str)
        ):
            super().add(chave, pagamento)

    def update(self, chave:str, pagamento: AbstractPagamento):
        if (
            pagamento is not None
            and isinstance(pagamento, AbstractPagamento)
            and isinstance(chave, str)
        ):
            super().update(chave, pagamento)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)
