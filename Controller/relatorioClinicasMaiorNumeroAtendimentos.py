from Controller.atendimentos import ControllerAtendimento
from Model.atendimento import Atendimento
from Model.clinica import Clinica


class ClinicasMaiorNumeroAtendimentos:
    def listar_clinicas_com_mais_atendimentos(self):
        atendimentos_por_clinica = {}
        for atendimento in ControllerAtendimento.listar_atendimentos():
            cnpj = atendimento.clinica.cnpj
            if cnpj in atendimentos_por_clinica:
                registros_atuais = atendimentos_por_clinica[cnpj]
                registros_atuais += 1
                atendimentos_por_clinica.update({cnpj:registros_atuais})
            else:
                atendimentos_por_clinica({cnpj:1})
        qt_atendimentos_ordenado = []
        for chave, valor in self.atendimentos_por_clinica.items():
            if len(qt_atendimentos_ordenado) == 0:
                qt_atendimentos_ordenado.append([chave, valor])
            elif valor <= qt_atendimentos_ordenado[len(qt_atendimentos_ordenado) - 1][2]:
                qt_atendimentos_ordenado.append([chave, valor])
            else:
                n = 0
                while n < len(qt_atendimentos_ordenado):
                    if valor > qt_atendimentos_ordenado[n][2]:
                        qt_atendimentos_ordenado.insert(n, [chave, valor])
                        break
                    n += 1
        return qt_atendimentos_ordenado
    # CONCLUIR
