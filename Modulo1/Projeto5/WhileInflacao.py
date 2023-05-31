uva = 5
uva2 = 10

produto = (input("Digite o nome da fruta: "))
while (produto != "uva"):
    produto = (input("Fruta indisponível, tente outra!: "))
print("O valor da uva atualmente é de: " + str(uva2) +
      "R$, " + "Semana passada era: " + str(uva) + "R$")
