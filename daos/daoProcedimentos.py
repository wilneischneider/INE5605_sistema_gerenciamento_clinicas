from daos.dao import DAO
from model.procedimento import Procedimento


class DaoProcedimentos(DAO):
    def __init__(self):
        super().__init__("procedimentos.pkl")

    def add(self, procedimento: Procedimento):
        if (
            procedimento is not None
            and isinstance(procedimento, Procedimento)
            and isinstance(procedimento.descricao, str)
        ):
            super().add(procedimento.descricao, procedimento)

    def update(self, procedimento: Procedimento):
        if (
            procedimento is not None
            and isinstance(procedimento, Procedimento)
            and isinstance(procedimento.descricao, str)
        ):
            super().update(procedimento.descricao, procedimento)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)
