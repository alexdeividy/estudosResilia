class Aluno():
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_matricula(self):
        return self.__matricula

aluno1 = Aluno("Alex", 19, 55501)

print(f"Aluno: {aluno1.get_nome()}, {aluno1.get_idade()} anos, Matrícula:{aluno1.get_matricula()}")