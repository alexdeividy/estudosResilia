class Casa():
    def __init__(self, endereco):
        self.endereco = endereco

    def get_endereco(self):
        return self.endereco
    
class Pessoa():
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
class Fatura():
    valor = ""
    def __init__(self, pessoa, endereco):
        self.valor = ""
        self.pessoa = pessoa
        self.endereco = endereco

    def mostra_fatura(self):
        print("A fatura de {} no endereco {} veio de {}".format(self.pessoa.get_nome(),self.endereco.get_endereco(),self.get_valor()))

    def get_valor(self):
        return self.valor


pessoa = Pessoa("Alex")
endereco = Casa("Av. Beberibe")
fatura = Fatura(pessoa, endereco)
fatura.valor = 900

fatura.mostra_fatura()

