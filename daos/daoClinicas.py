from daos.dao import DAO
from model.clinica import Clinica


class DaoClinicas(DAO):
    def __init__(self):
        super().__init__("clinicas.pkl")

    def add(self, clinica: Clinica):
        if (
            clinica is not None
            and isinstance(clinica, Clinica)
            and isinstance(clinica.cnpj, str)
        ):
            super().add(clinica.cnpj, clinica)

    def update(self, clinica: Clinica):
        if (
            clinica is not None
            and isinstance(clinica, Clinica)
            and isinstance(clinica.cnpj, str)
        ):
            super().update(clinica.cnpj, clinica)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)
