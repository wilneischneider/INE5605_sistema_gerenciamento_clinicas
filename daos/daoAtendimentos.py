from daos.dao import DAO
from model.atendimento import Atendimento


class DaoAtendimentos(DAO):
    def __init__(self):
        super().__init__("atendimentos.pkl")

    def add(self, atendimento: Atendimento):
        if (
            atendimento is not None
            and isinstance(atendimento, Atendimento)
        ):
            super().add(paciente.cpf, paciente) #{cpf_paciente:{data:{horario_inicio:atendimento}}}

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
