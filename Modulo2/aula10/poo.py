class ListaDeCompras():
    lista = []
    tamanho = 10

    def inserirItens(self):
        msg = input("Insira um item na lista: ")
        self.lista.append(msg)
    
    def consultarItens(self):
        print(self.lista)

listaJaneiro = ListaDeCompras()

listaJaneiro.inserirItens()
listaJaneiro.consultarItens()

print(listaJaneiro.tamanho)

while True:
    print("*"*30)
    print("1 - Inserir novo item")
    print("2 - Consultar itens")
    print("3 - Sair")
    print("*"*30,"\n")

    option = input("Digite uma opcao: ")
    if option == "3":
        break
    if option == "2":
        listaJaneiro.consultarItens()
    if option == "1":
        listaJaneiro.inserirItens()