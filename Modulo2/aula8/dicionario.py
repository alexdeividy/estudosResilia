portuIng = dict()
#portuIng["um"] = "one"
#print(len(portuIng))

#forma 02
inglesPortu = {"one" : "um", "two" : "dois", "three" : "tres"}
inglesPortu[3] = "zero"

print(inglesPortu)
print(len(inglesPortu))

if "one" in inglesPortu:
    print("Essa é uma chave valida 01")

if "um" in inglesPortu:
    print("Essa é uma chave valida 02")

#acessando valores das chaves
print(inglesPortu["two"], inglesPortu["three"])
print(inglesPortu.get(2))
print(inglesPortu.keys())

#acessar os valores pelos elementos
print(inglesPortu.values())

#retorna os itens do dicionaro no formato de tuplas
print(inglesPortu.items())

#alterar itens do dicionario
inglesPortu[0]= "zero"

#usando o metodo update
inglesPortu.update({"two" : "dos"})

#remover pela chave
inglesPortu.pop("one")
del inglesPortu["two"]

#remover pelo ultimo inserido
inglesPortu.popitem()

#esvaziar o dicionario inteiro
inglesPortu.clear()

print(inglesPortu)