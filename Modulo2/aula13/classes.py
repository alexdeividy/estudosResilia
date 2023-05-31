class Cliente():
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def get_nome(self):
        return self.nome
    
class Conta():
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

cliente = Cliente("Alex", "Santana", "999.999.999-99")
minhaConta = Conta("123-4", cliente, 120.0, 500.0)

print(cliente.get_nome())
print(minhaConta.saldo)