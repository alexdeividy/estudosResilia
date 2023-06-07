import csv 
import datetime

class Pesquisa():
    def __init__(self):
        self.__idade = ""
        self.__genero = ""
        self.respostas = []
#---------------------------------------------------------------#
    def valida_idade(self, idade):
        while True:
            if idade == "00":
                idade = self.valida_saida(idade)
                if idade == "00":
                    break
            else:
                try:
                    idade = int(idade)
                    return idade
                except ValueError:
                    print("Idade Inválida, Digite corretamente!")
                    idade = input("Digite sua idade novamente! ")
    #----------------------------------------------------------------#
    def valida_saida(self, idade):
        if idade == "00":
            while True:
                saida = input("\nDeseja sair da pesquisa? \n(1) Para sair\n(2) Para continuar\n Digite o número correspondente: ")
                if saida == "1":
                    print("Finalizando programa!")
                    exit()
                elif saida == "2":
                    idade = input("Digite sua idade novamente: ")
                    return self.valida_idade(idade)
                else:
                    print("\nDigite uma opção válida!")
        return idade
    #-----------------------------------------------------------------#
    def valida_genero(self, pergunta):
        generos = {
            "1": "Feminino",
            "2": "Masculino",
            "3": "Outro",
            "4": "Não quero responder"
        }
        while True:
            resposta = input(pergunta)
            if resposta in generos:
                return generos[resposta]
            else:
                print("Resposta inválida, digite apenas números de 1 a 4!")
    #-----------------------------------------------------------------------#
    def obter_idade(self):
        self.__idade = self.valida_idade(input("\nSe desejar sair do programa, digite: 00\n\nDigite sua idade: "))

    def get_idade(self):
        return self.__idade

    def obter_genero(self):
        self.__genero = self.valida_genero("\n Você se identifica com qual gênero?\n(1) Feminino\n(2) Masculino\n(3) Outro\n(4) Não quero responder\n Digite o número correspondente: ")

    def get_genero(self):
        return self.__genero
    #---------------------------------------------------------------------------------------------------------------------------------------------------#
    def valida_resposta(self, pergunta):
        opcoes = {
            "1": "Sim",
            "2": "Não",
            "3": "Não quero responder"
        }
        while True:
            resposta = input(pergunta)
            if resposta in opcoes:
                return opcoes[resposta]
            else:
                print("Resposta inválida, digite números de 1 a 3!")
    #----------------------------------------------------------------#
    def questionario(self):
        respostas_usuario = {}
        respostas_usuario["idade"] = self.get_idade()
        respostas_usuario["genero"] = self.get_genero()

        respostas_usuario["pergunta1"] = self.valida_resposta(
        "\n Você costuma jogar games Multiplayer?\n(1) Sim\n(2) Não\n(3) Não quero responder\n Digite o número correspondente: ")

        respostas_usuario["pergunta2"] = self.valida_resposta(
        "\n Você costuma jogar games Singleplayer?\n(1) Sim\n(2) Não\n(3) Não quero responder\n Digite o número correspondente: ")

        respostas_usuario["pergunta3"] = self.valida_resposta(
        "\n Você costuma jogar em dispositívos portáteis?\n(1) Sim\n(2) Não\n(3) Não quero responder\n Digite o número correspondente: ")

        respostas_usuario["pergunta4"] = self.valida_resposta(
        "\n Você costuma jogar em dispositivos de mesa?\n(1) Sim\n(2) Não\n(3) Não quero responder\n Digite o número correspondente: ")

        respostas_usuario["date_time"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        self.respostas.append(respostas_usuario)
    #----------------------------------------------------------------------------------------------------------------------------------------#
    def mostra_respostas(self):
        ultimo_usuario = self.respostas[-1]
        print(f"\nRespostas na base de dados: \nIdade = {self.get_idade()} \nGênero = {self.get_genero()} \nPergunta 1 = {ultimo_usuario['pergunta1']} \nPergunta 2 = {ultimo_usuario['pergunta2']} \nPergunta 3 = {ultimo_usuario['pergunta3']} \nPergunta 4 = {ultimo_usuario['pergunta4']}")

    def criar_csv(self):
        with open("Pesquisa_Games.csv", "w", newline="", encoding="utf-8") as pesquisa_csv:
            fieldnames = list(self.respostas[0].keys())
            writer = csv.DictWriter(pesquisa_csv, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.respostas)
#----------------------------------------------------------------------------------------------------------------------------------------------#
video_games = Pesquisa()

while True:
    print("\n Bem vindo a pesquisa de Jogos!")
    video_games.obter_idade()
    video_games.obter_genero()
    video_games.questionario()
    video_games.mostra_respostas()
    video_games.criar_csv()
    print()
    print("Obrigado por responder nossa pesquisa!")