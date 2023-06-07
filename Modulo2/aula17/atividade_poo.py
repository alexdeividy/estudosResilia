import datetime
class Categorias():
    def __init__(self, titulo):
        self.titulo = titulo
    
class Eventos(Categorias):
    def __init__(self, titulo, data, categorias):
        self.titulo = titulo
        self.data = data
        self.lista_categorias = categorias
        
    def criar_evento(self):
        print(self.titulo)
        self.data = data_atual
        print("Categorias disponíveis",lista_categorias)

def data_atual():
    data = print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    return data 


lista_categorias = ["Miranha", "Xuxa", "Hulk"]
data = data_atual()


evento1 = Eventos("Aniversário", data_atual(), lista_categorias)
evento1.criar_evento()

# abre o arquivo em modo "append"
salvar = open("teste.txt", "a")
salvar.write("Ola mundo\n")
salvar.close()