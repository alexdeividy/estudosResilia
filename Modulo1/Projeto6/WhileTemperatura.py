while True:
    temperatura = (input("Digite sua temperatura: "))
    if (temperatura != "sair"):
        temperatura = float(temperatura)
        if (temperatura >= 39):
            print("Você está com febre alta!")
        elif (temperatura <= 37.9):
            print("Você não está com febre!")
        else:
            print("Você está com febre mediana!")
    else:
        print("Você saiu do programa!")
        break
