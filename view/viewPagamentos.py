from view import superView


class ViewPagamentos(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE PAGAMENTOS ---------")
        print("Escolha sua opção:")
        print("1 - Realizar Pagamento")
        print("2 - Consultar Pagamentos")
        print("3 - Listar Pagamentos")
        print("4 - Consultar Saldo Devedor")
        print("0 - Retornar")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4])
        return opcao

    def pegar_cpf_pagador(self):
        cpf = input("CPF do(a) Pagador(a): ")
        return cpf

    def pegar_dados_do_cartao(self):
        numero = input("Número do Cartão de Crédito: ")
        bandeira = input("Bandeira do Cartão: ")
        return {"numero": numero, "bandeira": bandeira}

    def pegar_cpf_paciente(self):
        cpf_paciente = input("Informe o CPF do Paciente: ")
        return cpf_paciente

    def mostrar_pagamentos_paciente(self, dados):
        for pagamento in dados:
            print(f'Data: {pagamento["data"]}, Valor: {pagamento["valor"]}')

    def mostrar_pagamentos(self, dados):
        for pagto in dados:
            print(f'Paciente: {pagto["nome_paciente"]} [{pagto["cpf_paciente"]}], Data: {pagto["data"]}, Valor: R$ {pagto["valor"]}')

    def mostrar_valores_em_aberto(self, dados):
        print("--- Débitos do Paciente ---")
        for atendimento in dados["atendimentos"]:
            print(f'Data: {atendimento["data"]}, Horário: {atendimento["horario"]},'
                  f' Valor do Atendimento: {atendimento["valor_atendimento"]},'
                  f' Valor dos Procedimentos: {atendimento["valor_procedimentos"]}')
        print(f'Total Pago: R$ {dados["total_pago"]}')
        print(f'SALDO DEVEDOR: R$ {dados["saldo"]}')

    def pegar_data_da_consulta(self):
        repetir = 0
        while repetir == 0:
            ano_consulta = input("Informe o Ano da Consulta (AAAA): ")
            mes_consulta = input("Informe o Mês da Consulta (MM): ")
            dia_consulta = input("Informe o Dia da Consulta (DD): ")
            try:
                ano = int(ano_consulta)
                mes = int(mes_consulta)
                dia = int(dia_consulta)
                data_consulta = Date(ano, mes, dia)
                repetir = 1
            except ValueError:
                print("Informe ano, mês e dia em numerais, nos formatos indicados. Ex.: Ano: 1990, Mês: 5, Dia: 15")
        return data_consulta

    def pegar_horario_da_consulta(self):
        repetir = 0
        while repetir == 0:
            hora_consulta = input("Informe a Hora de Início da Consulta (HH): ")
            minuto_consulta = input("Informe os Minutos de Início da Consulta (MM): ")
            try:
                hora = int(hora_consulta)
                minuto = int(minuto_consulta)
                horario_inicio = Time(hora, minuto)
                repetir = 1
            except ValueError:
                print("Informe hora e minutos em numerais, nos formatos indicados. Ex.: Hora: 18, Minuto: 27")
        return horario_inicio

    def pegar_data_de_pagamento(self):
        repetir = 0
        while repetir == 0:
            ano_pagamento = input("Informe o Ano do Pagamento (AAAA): ")
            mes_pagamento = input("Informe o Mês do Pagamento (MM): ")
            dia_pagamento = input("Informe o Dia do Pagamento (DD): ")
            try:
                ano = int(ano_pagamento)
                mes = int(mes_pagamento)
                dia = int(dia_pagamento)
                data_pagamento = Date(ano, mes, dia)
                repetir = 1
            except ValueError:
                print("Informe ano, mês e dia em numerais, nos formatos indicados. Ex.: Ano: 1990, Mês: 5, Dia: 15")
        return data_pagamento

    def pegar_valor_do_pagamento(self):
        repetir = 0
        while repetir == 0:
            valor = input("Valor do Pagamento (em R$): ")
            try:
                valor = float(valor)
                repetir = 1
            except ValueError:
                print("Informe apenas valores, utilizando ponto '.' como separador de decimal.")
        return valor

    def pegar_numero_parcelas(self):
        repetir = 0
        while repetir == 0:
            valor = input("Informe o número de parcelas: ")
            try:
                valor = int(valor)
                if valor > 0:
                    repetir = 1
                else:
                    print("Informe um valor inteiro maior que zero.")
            except ValueError:
                print("Informe um valor inteiro maior que zero.")
        return valor

    def selecionar_forma_de_pagamento(self):
        print("--- Selecione a Forma de Pagamento---")
        print("Escolha sua opção:")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão de Crédito")
        print("0 - Retornar")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0, 1, 2, 3])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
