def dirigirOuBeber(idade):
    if (idade < 18):
        return print("Não pode dirigir e nem beber!")
    else:
        return print("Pode beber ou dirigir")


idade1 = int(input("Digite sua idade: "))
dirigirOuBeber(idade1)
