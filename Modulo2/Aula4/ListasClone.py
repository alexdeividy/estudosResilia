nomes = ["Rafael", "Will", "Jose", "Vic", "Alex"]
#print(nomes[::2])

#lista_copia = nomes
lista_copia = nomes[:]

nomes[1] = "Univitelinas"

print(nomes)
print(lista_copia)