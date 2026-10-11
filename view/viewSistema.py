from view.superView import SuperView


class ViewSistema(SuperView):
    def view_opcoes(self):
        print("-------- SISTEMA DE GERENCIAMENTO DE CLÍNICAS ---------")
        print("Escolha sua opção:")
        print("1 - Gerenciar Atendimentos")
        print("2 - Gerenciar Pagamentos")
        print("3 - Gerenciar Pacientes")
        print("4 - Gerenciar Procedimentos")
        print("5 - Gerenciar Profissionais")
        print("6 - Gerenciar Clínicas")
        print("7 - Emitir Relatórios")
        print("0 - Finalizar sistema")
        opcao = self.entra_opcao_valida("Escolha a opção desejada: ", [0,1,2,3,4,5,6,7])
        return opcao
