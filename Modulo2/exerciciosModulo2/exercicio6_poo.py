class Animal():
    def __init__(self, nome, som_animal):
        self.nome = nome
        self.som_animal = som_animal

    def falar(self):
        return print(f"O animal fez: {self.som_animal}")

gato = Animal("Joao", "Miau")

print(gato.nome)
print(gato.som_animal)
gato.falar()