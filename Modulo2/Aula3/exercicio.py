
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = [0] * 10
for i in range(10):
    resultado[i] = lista1[i] * (lista2[i])

print(resultado)
