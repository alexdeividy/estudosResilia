def maiorDeles(valor1, valor2, valor3):
    if valor1 > valor2 and valor1 > valor3:
        print(valor1)
    elif valor2 > valor1 and valor2 > valor3:
        print(valor2)
    elif valor3 > valor1 and valor3 > valor2:
        print(valor3)

maiorDeles(5, 10, 15)