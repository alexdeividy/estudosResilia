class Produto():
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco

produto1 = Produto("Arroz", "5.99")

print(f"O {produto1.get_nome()} custa: {produto1.get_preco()}")