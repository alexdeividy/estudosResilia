telefones = {
    ("ana", "santos") : "5555-5555",
    ("maria", "lurdes") : "5555-8888",
    ("jessica", "pereira") : "2222-5555"
}

for nome, sobrenome in telefones:
    print(nome, sobrenome)

print(telefones[("maria", "lurdes")])