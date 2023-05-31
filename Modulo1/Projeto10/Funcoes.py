def soma(valor1, valor2):
    return valor1+valor2


def printSoma(valor1, valor2, resultado, dobro):
    return print(f"A soma do {valor1} mais o {valor2} é igual ao {resultado} e seu dobro é igual ao {dobro}")


def calculaDobroDaSoma(valor1, valor2):
    resultado = soma(valor1, valor2)
    dobro = resultado * 2
    return printSoma(valor1, valor2, resultado, dobro)


(calculaDobroDaSoma(5, 5))
