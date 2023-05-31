numeroPacientes = int(input("Digite o número de pacientes: "))
for i in range ((numeroPacientes)):
    nome = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    altura = altura**2
    imc = peso / altura
    print("Paciente: ",nome ,"Seu IMC eh de: ",imc)

