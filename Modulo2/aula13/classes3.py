class Historico():
    def __init__(self):
        self.data_abertura = ""
        self.transacoes = []

class Conta():
    def __init__(self):
        self.cliente = ""
        self.historico = Historico()

minha_conta = Conta()
minha_conta.cliente = "Alex"
minha_conta.historico.transacoes = [1,2,3]
minha_conta.historico.data_abertura = "30/05/2023"

print(minha_conta.historico.transacoes)
print(minha_conta.historico.data_abertura)