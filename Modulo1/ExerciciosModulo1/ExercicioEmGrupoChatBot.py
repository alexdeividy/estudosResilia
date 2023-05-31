import funcoesChatBot as fchat

print('Bem-vindo à Barbearia 90S')
nome = (input('Qual seu nome? '))
print('Olá', nome)

selecione = 0
while selecione == 0:
    fchat.escolhas(
        valor1='\n1. Serviços\n2. Agendamento\n3. Dúvidas\n4. Sair\n')
    selecione = (int(input("Escolha uma opção para começar: ")))

    if selecione == 3:
        while selecione == 3:
            resposta = int(input(
                '\n1. Horário de funcionamento.\n2. Localização.\n3. Formas de pagamento\n4. Outras dúvidas\n5. Sair\n\nEscolha uma opção para prosseguir: '))
            while resposta != 5:
                if resposta == 1:
                    simNao = input(
                        "\nFuncionamos das 08:00 as 22:00!\nSegunda a Sexta-Feira ;)\n\nDeseja algo mais? (sim/não): ")
                    if simNao == "sim":
                        selecione = 0
                        break
                    else:
                        print("Obrigado, volte sempre!")
                        break
                elif resposta == 2:
                    simNao = input(
                        "\nEstamos localizados na rua Ifood, n50, Resilia, 50500-500\n\nDeseja algo mais? (sim/não): ")
                    if simNao == "sim":
                        selecione = 0
                        break
                    else:
                        print("Obrigado, volte sempre!")
                        break
                elif resposta == 3:
                    simNao = input(
                        "\nCrédito, Débito, Dinheiro e PIX\n\nDeseja algo mais? (sim/não): ")
                    if simNao == "sim":
                        selecione = 0
                        break
                    else:
                        print("Obrigado, volte sempre!")
                        break
                elif resposta == 4:
                    simNao = input(
                        "\nPara sanar outras dúvidas, entre em contato conosco pelo número: (50)95050-5050\n\nDeseja algo mais? (sim/não): ")
                    if simNao == "sim":
                        selecione = 0
                        break
                    else:
                        print("Obrigado, volte sempre!")
                        break
            print("Obrigado, volte sempre!")
            break
