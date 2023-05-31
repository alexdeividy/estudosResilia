class Pessoa():
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

# Getters and Setters #
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome
    def get_cpf(self):
        return self._cpf
    def set_cpf(self, cpf):
        self._cpf = cpf

# Criacao dos objetos, pessoa1, e pessoa2
pessoa1 = Pessoa("Alex", "999.999.999-99")
pessoa2 = Pessoa("Rafael", "000.000.000-00")

# mostra os atributos dos objetos: pessoa1, e pessoa2
print(f"A primeira pessoa da lista e: {pessoa1.get_nome()}, de CPF: {pessoa1.get_cpf()}")
print(f"A Segunda pessoa da lista e: {pessoa2.get_nome()}, de CPF: {pessoa2.get_cpf()}")
print()

# altera o nome da pessoa1
pessoa1.set_nome("Deividy")
# altera o cpf da pessoa2
pessoa2.set_cpf("555.555.555-55")

# mostra os atributos ja alterados dos objetos: pessoa1, e pessoa2
print(f"A primeira pessoa da lista e: {pessoa1.get_nome()}, de CPF: {pessoa1.get_cpf()}")
print(f"A Segunda pessoa da lista e: {pessoa2.get_nome()}, de CPF: {pessoa2.get_cpf()}")