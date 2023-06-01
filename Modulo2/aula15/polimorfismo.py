#Polimorfismo

class Funcionario():
    def comissao(self, valor):
        print(valor *0.5)

class Supervisor(Funcionario):
    def comissao(self, valor):
        print(valor *1.5)

class Gerente(Funcionario):
    def comissao(self, valor):
        print(valor *2)

rafael = Funcionario()
daniel = Supervisor()
danylo = Gerente()

rafael.comissao(100)
daniel.comissao(100)
danylo.comissao(100)
