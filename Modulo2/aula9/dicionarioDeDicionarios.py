#DICIONARIO DE DICIONARIOS

#varios dicionarios
carro01 = {"cor" : "preto", "motor" : 1.0, "ano" :2008}
carro02 = {"cor" : "branco", "motor" : 1.4, "ano" :2023}
carro03 = {"cor" : "cinza", "motor" : 1.8, "ano" :2018}
carro04 = {"cor" : "azul", "motor" : 1.6, "ano" :2015}

dicCarros = {
    "Gol" : carro01,
    "Civic" : carro02,
    "Marea" : carro03,
    "Monza" : carro04,
    "Hilux" : carro03
}

for elemento in dicCarros.items():
    print(elemento)