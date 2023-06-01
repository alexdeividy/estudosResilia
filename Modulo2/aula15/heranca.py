#Herança

class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, senha, qtd_funcionarios):
        self.senha = senha
        self.qtd_funcionarios = qtd_funcionarios

funcionario = Funcionario('rafael', '111.111.111-11', 123)
print(funcionario.salario)
gerente = Gerente('123456', 4)
gerente.salario = 456
print(gerente.salario)