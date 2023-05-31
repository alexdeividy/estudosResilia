numero = int(input("Digite um numero: "))

def fatorial(valor):
    for n in range(1, valor*1):
        valor = valor * n
    print(valor)

fatorial(numero)