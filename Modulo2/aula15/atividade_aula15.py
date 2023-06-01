#Atividade Herança e Polimorfismo

class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn

class Ebook(Livro):
    def __init__(self, link_download):
        self.link_download = link_download

livro1 = Livro('Cinderela', '9783314103926')

livro1_ebook = Ebook('cinderela.download.compre_o_livro')
livro1_ebook.titulo = 'Cinderela'

print(f'Nome: {livro1.titulo} // ISBN: {livro1.isbn}')
print(F'nome: {livro1_ebook.titulo} // Link: {livro1_ebook.link_download}')