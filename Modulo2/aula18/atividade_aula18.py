class Armazena():
    def __init__(self):
        self.lista = []

    def guarda_entrada(self, entrada):
        entrada = self.lista.append(entrada)

    def descarta_entrada(self):
        self.lista.pop(0)


entrada1 = input("Digite qualquer coisa: ")
entrada2 = input("Digite qualquer coisa pela segunda vez: ")
entrada3 = input("Digite qualquer coisa pela terceira vez: ")
entrada4 = input("Digite tal: ")

entradas = Armazena()

entradas.guarda_entrada(entrada1)
entradas.guarda_entrada(entrada2)
entradas.guarda_entrada(entrada3)
entradas.guarda_entrada(entrada4)
print(entradas.lista)

entradas.descarta_entrada()
entradas.descarta_entrada()
print(entradas.lista)

