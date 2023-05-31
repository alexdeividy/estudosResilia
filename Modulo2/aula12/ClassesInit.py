class Carro():
    cor = "amarelo"
    def __init__(self, rodas, capacidadeDeTanque):
        self.rodas = rodas
        self.qtdLitrosTanque = capacidadeDeTanque

    def get_cor(self):
        return self.cor
    
    def set_cor(self, novaCor):
        self.cor = novaCor

amelie = Carro(4, 50)
print(amelie.get_cor())
amelie.set_cor("azul")
print(amelie.get_cor())