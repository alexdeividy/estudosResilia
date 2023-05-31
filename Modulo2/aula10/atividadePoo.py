class Cachorro():
    nome = []
    nascimento = []

    def inserirNome(self):
        msg = input("Insira o nome do Cachorro: ")
        self.nome.append(msg)
    
    def inserirNascimento(self):
        msg = input("Insira a data de nascimento: ")
        self.nascimento.append(msg)

    def latir(self):
        msg = input("Digite '1' para Latir ")
        if msg == "1":
            print("O cachorro latiu")

    def comer(self):
        msg = input("Digite '2' para Comer ")
        if msg == "2":
            print("O cachorro comeu")
    
    def mostrarCachorro(self):
        msg = input("Digite '3' para mostrar os dados do Cachorro ")
        if msg == "3":
            print("Nome:",cachorro.nome, "Nascimento:",cachorro.nascimento)

cachorro = Cachorro()

cachorro.inserirNome()
cachorro.inserirNascimento()
cachorro.latir()
cachorro.comer()
cachorro.mostrarCachorro()
