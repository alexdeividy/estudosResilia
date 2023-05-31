class Pessoa():
    idade = ""
    cidade = ""
    estado = ""
    salarioAtual = ""
    escolaridade = ""

    def imprimirDados(self,idade,cidade,estado,salarioAtual,escolaridade):
        print(f"{idade},{cidade},{estado},{salarioAtual},{escolaridade}")

alex = Pessoa()

alex.idade = "21"
alex.cidade = "Recife"
alex.estado = "PE"
alex.salarioAtual = "R$1000"
alex.escolaridade = "Superior-Cursando"

alex.imprimirDados(alex.idade,alex.cidade,alex.estado,alex.salarioAtual,alex.escolaridade)