lista1 = [1, 2, 3]
lista2 = [3, 2, 1]
lista3 = []

for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)