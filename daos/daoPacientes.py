from daos.dao import DAO
from model.paciente import Paciente


class DaoPacientes(DAO):
    def __init__(self):
        super().__init__("pacientes.pkl")

    def add(self, paciente: Paciente):
        if (
            paciente is not None
            and isinstance(paciente, Paciente)
            and isinstance(paciente.cpf, str)
        ):
            super().add(paciente.cpf, paciente)

    def update(self, paciente: Paciente):
        if (
            paciente is not None
            and isinstance(paciente, Paciente)
            and isinstance(paciente.cpf, str)
        ):
            super().update(paciente.cpf, paciente)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)
