#Adiciona na pilha
def inserirNaPilha(pilha, elemento1):
    return pilha.append(elemento1)

# Remove da Pilha
def retirarNaPilha(pilha):
    return pilha.pop(-1)

# Mostra o tamanho da Pilha
def tamanhoDaPilha(pilha):
    return print(len(pilha))

# Verifica se a pilha esta vazia (com a funcao TamanhoDaPilha embutido)
def pilhaVazia(pilha):
    tamanhoDaPilha(pilha)
    if len(pilha) == 0:
        print("Lista vazia!")
    else:
        print("A lista não está vazia") 

# Pilha vazia
pilha = []

# Chamada da Funcao de Inserir elementos na Pilha
inserirNaPilha(pilha, "Marcos")
inserirNaPilha(pilha, "Julia")
inserirNaPilha(pilha, "Rafael")
print(pilha)

# Chamada da Funcao de Remover elementos na Pilha
retirarNaPilha(pilha)
print(pilha)

#tamanhoDaPilha(pilha)
pilhaVazia(pilha)
