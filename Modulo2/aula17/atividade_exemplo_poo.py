import datetime

def obter_data_hora():
    data_hora = datetime.datetime.now()
    return data_hora.strftime("%d/%m/%Y %H:%M:%S")

class Categoria():
    def __init__(self, titulo_categoria):
        self.titulo_categoria = titulo_categoria

class Eventos(Categoria):
    def __init__(self, titulo_eventos, data_hora):
        self.titulo_eventos = titulo_eventos
        self.data_hora = data_hora()

categorias = ["LOL", "CS:GO", "VALORANT", "DOTA"]
print(categorias)

input_categoria = input("Insira o título da categoria: ")
input_evento = input("Insira o evento: ")

evento = Eventos(input_evento, obter_data_hora)
evento.titulo_categoria = input_categoria

salvar = open("teste.txt", "a")
salvar.write(f"{evento.titulo_categoria}, {evento.titulo_eventos}, {evento.data_hora}\n")
salvar.close()