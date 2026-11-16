from daos.dao import DAO
from model.profissional import Profissional


class DaoProfissionais(DAO):
    def __init__(self):
        super().__init__("profissionais.pkl")

    def add(self, profissional: Profissional):
        if (
            profissional is not None
            and isinstance(profissional, Profissional)
            and isinstance(profissional.cpf, str)
        ):
            super().add(profissional.cpf, profissional)

    def update(self, profissional: Profissional):
        if (
            profissional is not None
            and isinstance(profissional, Profissional)
            and isinstance(profissional.cpf, str)
        ):
            super().update(profissional.cpf, profissional)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)
