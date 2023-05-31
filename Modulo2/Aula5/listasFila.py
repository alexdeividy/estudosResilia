def inserirNaFila(fila, elemento1):
    return fila.append(elemento1)

def retirarNaFila(fila):
    return fila.pop(0)

fila = []

inserirNaFila(fila, "Marcos")
inserirNaFila(fila, "Julia")
inserirNaFila(fila, "Rafael")
print(fila)

retirarNaFila(fila)
print(fila)
