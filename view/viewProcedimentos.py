from view import superView


class ViewProcedimentos(SuperView):
    def view_opcoes(self):
        print("-------- MÓDULO DE GESTÃO DE PROCEDIMENTOS ---------")
        print("Escolha sua opção:")
        print("1 - Gerenciar Atendimentos")
        print("2 - Gerenciar Pagamentos")
        print("3 - Gerenciar Pacientes")
        print("4 - Gerenciar Procedimentos")
        print("5 - Gerenciar Profissionais")
        print("6 - Gerenciar Clínicas")
        print("0 - Finalizar sistema")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6])
        return opcao
