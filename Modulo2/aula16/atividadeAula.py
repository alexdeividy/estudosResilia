class Funcionario():
    def __init__(self, nome):
        self.nome = nome
        self.salario_base = 1000

    def calcular_salario(self):
        return self.salario_base

class FuncionarioClt(Funcionario):
    tempo_empresa = ""

    def calcular_salario(self):
        return self.salario_base * (self.tempo_empresa / 100)

class FuncionarioPj(Funcionario):
    senioridade = 0

    def calcular_salario(self):
        return self.salario_base * (self.senioridade)

alex = FuncionarioClt("Alex")
jeff = FuncionarioPj("Jeff")

jeff.senioridade = 3
alex.tempo_empresa = 6

print(f"O salário do Funcionário {alex.nome} é {alex.calcular_salario()}")
print(f"O salário do Funcionário {jeff.nome} é {jeff.calcular_salario()}")
