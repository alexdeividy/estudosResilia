tomate1 = 5
laranja1 = 10
abacaxi1 = 15
limao1 = 20

tomate2 = 10
laranja2 = 5
abacaxi2 = 15
limao2 = 20

produto = (input("Digite o nome do produto: "))
if (produto == "tomate"):
    if (tomate2 > tomate1):
        print("O valor do Tomate aumentou:", tomate2 - tomate1 ,"R$, em relação a semana passada!")
    elif (tomate2 < tomate1):
        print("O valor do Tomate diminuiu:", tomate1 - tomate2 ,"R$, em relação a semana passada!")
    else:
        print("O valor do Tomante se manteve o mesmo!")
elif (produto == "laranja"):
    if (laranja2 > laranja1):
        print("O valor da Laranja aumentou: " + str(laranja2 - laranja1) + "R$ em relação a semana passada!")
    elif (laranja2 < laranja1):
        print("O valor da Laranja diminuiu: " + str(laranja1 - laranja2) + "R$ em relação a semana passada!")
    else:
        print("O valor da Laranja se manteve o mesmo!")
elif (produto == "abacaxi"):
    if (abacaxi2 > abacaxi1):
        print("O valor do Abacaxi aumentou:", abacaxi2 - abacaxi1 ,"R$, em relação a semana passada!")
    elif (abacaxi2 < abacaxi1):
        print("O valor do Abacaxi diminuiu:", abacaxi1 - abacaxi2 ,"R$, em relação a semana passada!")
    else:
        print("O valor do Abacaxi se manteve o mesmo!")
elif (produto == "limao"):
    if (limao2 > limao1):
        print("O valor do Limão aumentou:", limao2 - limao1 ,"R$, em relação a semana passada!")
    elif (limao2 < limao1):
        print("O valor do Limão diminuiu:", limao1 - limao2 ,"R$, em relação a semana passada!")
    else:
        print("O valor do Limão se manteve o mesmo!")
else:
    print("Digite um produto disponível!")
