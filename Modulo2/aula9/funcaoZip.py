#funcao zip
lista01 = [1, 2, 3, 4, 5]
lista02 = ["a", "b", "c", "d", "e"]

for item1, item2 in zip(lista01, lista02):
    print(f"item 1: {item1} item 2: {item2}")