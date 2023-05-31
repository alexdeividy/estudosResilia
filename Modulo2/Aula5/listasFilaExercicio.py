def inserirNaFila(fila, elemento1):
    return fila.append(elemento1)

def retirarNaFila(fila):
    return fila.pop(0)

def tamanhoDaFila(fila):
    return print(len(fila))

def filaVazia(fila):
    if len(fila) == 0:
        print("Lista vazia!")
    else:
        print("A lista não está vazia") 


fila = []

inserirNaFila(fila, "Marcos")
inserirNaFila(fila, "Julia")
inserirNaFila(fila, "Rafael")
print(fila)

retirarNaFila(fila)
print(fila)

#tamanhoDaFila(fila)
filaVazia(fila)
