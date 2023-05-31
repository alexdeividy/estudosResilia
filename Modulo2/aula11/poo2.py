class Gato():
    nome = ""
    dataDeNascimento = ""
    raca = ""

    def miar(self, nome):
        print("O gato",nome,"miou!!")

    def comer(self, nome):
        print("O gato",nome,"comeu!!")

meuGato = Gato()

meuGato.nome = "Rafael"
meuGato.dataDeNascimento = "19/03/2020"
meuGato.raca = "Frajola"
meuGato.miar(meuGato.nome)
meuGato.comer(meuGato.nome)
print(meuGato.nome)
print(meuGato.dataDeNascimento)
print(meuGato.raca)