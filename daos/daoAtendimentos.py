from daos.dao import DAO
from model.atendimento import Atendimento


class DaoAtendimentos(DAO):
    def __init__(self):
        super().__init__("atendimentos.pkl")

    def add(self, cpf_paciente:str, atendimentos: dict):
        if (
            cpf_paciente is not None
            and atendimentos is not None
            and isinstance(cpf_paciente, str)
            and isinstance(atendimentos, dict)
        ):
            super().add(cpf_paciente, atendimentos) #{cpf_paciente:{data:{horario_inicio:atendimento}}}

    def update(self, cpf_paciente:str, atendimentos: dict):
        if (
            cpf_paciente is not None
            and atendimentos is not None
            and isinstance(cpf_paciente, str)
            and isinstance(atendimentos, dict)
        ):
            super().add(cpf_paciente, atendimentos)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)
