class Desfazer_refazer():
    def __init__(self):
        self.lixeira = []
        self.guarda_entradas = []

    def adiciona(self):
        self.entrada = input("Digite algo: ")
        self.guarda_entradas.append(self.entrada)
    
    def exclui(self):
        self.comando = input("Digite 1 para excluir a última entrada: ")
        if self.comando == "1":
            self.lixeira.append(self.guarda_entradas[-1])
            self.guarda_entradas.pop(-1)
        
    def desfazer(self):
        self.comando = input("Digite 1 para desfazer a exclusão: ")
        if self.comando == "1":
            self.guarda_entradas.append(self.lixeira[0])
            self.lixeira.pop(0)
        

objeto = Desfazer_refazer()

objeto.adiciona()
print(objeto.guarda_entradas)
print(objeto.lixeira)
objeto.exclui()
print(objeto.guarda_entradas)
print(objeto.lixeira)
objeto.desfazer()
print(objeto.guarda_entradas)
print(objeto.lixeira)