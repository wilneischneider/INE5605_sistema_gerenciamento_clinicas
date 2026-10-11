class HorarioForaDoHorarioDaClinicaException(Exception):
    def __init__(self, horario_da_clinica:dict):
        self.mensagem = f'Fora do horário de atendimento. A clínica funciona das {horario_da_clinica["abre"]} às {horario_da_clinica["fecha"]}.'
        super().__init__(self.mensagem)
