tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla2 = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
tupla3 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)



for i in range(len(tupla3)):
    tupla3 = tupla1[i] * tupla2[i]
    print(tupla3)
