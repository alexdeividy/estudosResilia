glossario = dict()
glossario = {"print" : "A função print, mostra na tela para o usuário qualquer informação do código",
             "str" : "O tipo 'str' quer dizer (Caracteres), e serve para definir valores como letras",
             "int" : "O tipo 'int' quer dizer (Inteiro), e serve para definir valores como números inteiros",
             "input" : "A função 'input' quer dizer (Entrada), e serve para absorver valores digitados pelo usuário",
             "float" : "O tipo 'float' quer dizer (Flutuante), e serve para definir valores como números quebrados"}

glossario["while"] = "Estrutura de repetição (Enquanto)"
glossario.update({"print" : "Função print atualizada!"})

glossario.pop("str")
del glossario["int"]
glossario.popitem()

print("\Termos disponíveis no programa:",glossario.keys())

while True:
    palavraUsuario = input("\nDigite um termo de programação e iremos mostrar seu significado: ")

    if palavraUsuario in glossario:
        print("\n",glossario.get(palavraUsuario))

    break

glossario.clear()
print(glossario)
