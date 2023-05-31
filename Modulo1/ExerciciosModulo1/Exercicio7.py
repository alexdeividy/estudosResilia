salario = int(input("Digite o seu salario: "))

if salario <= 600:
    print("Voce eh isento")
elif salario <= 1200:
    salario = salario * 0.8
    print("Seu desconto eh de 20%, e seu salario ficou: ",salario)
elif salario <= 2000:
    salario = salario * 0.75
    print("Seu desconto eh de 25%, e seu salario ficou: ",salario)
else:
    salario = salario * 0.70
    print("Seu desconto eh de 30%, e seu salario ficou: ",salario)