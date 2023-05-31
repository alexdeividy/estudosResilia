lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for i in range(15):
    if (i % 2) != 0:
        lista.pop(lista.index(i))
    lista.sort(reverse=True)
print(lista)