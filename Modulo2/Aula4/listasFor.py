frutas = ["figo", "banana", "kiwi", "melancia", "pera", "blueberry"]

nova_lista = [i for i in frutas if "a" not in i]
# for i in frutas:
#     if "a" not in i:
#         nova_lista.append(i)

maiusculo = [i.title() for i in frutas]

print(maiusculo)
print(nova_lista)