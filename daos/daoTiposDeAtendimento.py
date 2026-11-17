from daos.dao import DAO
from model.tipoDeAtendimento import TipoDeAtendimento


class DaoTipoDeAtendimento(DAO):
    def __init__(self):
        super().__init__("tipoDeAtendimento.pkl")

    def add(self, tipoDeAtendimento: TipoDeAtendimento):
        if (
            tipoDeAtendimento is not None
            and isinstance(tipoDeAtendimento, TipoDeAtendimento)
        ):
            super().add(tipoDeAtendimento.tipo, tipoDeAtendimento)

    def update(self, tipoDeAtendimento: TipoDeAtendimento):
        if (
            tipoDeAtendimento is not None
            and isinstance(tipoDeAtendimento, TipoDeAtendimento)
        ):
            super().update(tipoDeAtendimento.tipo, tipoDeAtendimento)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)
