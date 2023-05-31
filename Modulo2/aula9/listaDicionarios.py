#LISTA DE DICIONARIOS

#varios dicionarios
carro01 = {"cor" : "preto", "motor" : 1.0, "ano" :2008}
carro02 = {"cor" : "branco", "motor" : 1.4, "ano" :2023}
carro03 = {"cor" : "cinza", "motor" : 1.8, "ano" :2018}
carro04 = {"cor" : "azul", "motor" : 1.6, "ano" :2015}

listaCarros = [carro01, carro02, carro03, carro04]

for carro in listaCarros:
    print(carro)

print(listaCarros[0]["cor"])
print(listaCarros[1]["motor"])