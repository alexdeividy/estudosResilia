inglesPortu = {"one" : "um", "two" : "dois", "three" : "tres"}

#iterar elementos no dicionario

for chave in inglesPortu:
    print(f"O item {chave} possui o valor {inglesPortu[chave]} no dicionario")

for chave, valor in inglesPortu.items():
    print(f"Os valores da tupla são {chave} e {valor}")