idAluno = int(input("Escreva sua identificação: "))
nota1 = float(input("Escreva sua primeira nota: "))
nota2 = float(input("Escreva sua segunda nota: "))
nota3 = float(input("Escreva sua terceira nota: "))
me = float(input("Escreva sua média de exercícios: "))

ma = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7

print("Olá Aluno! identificação de número: " +
      str(idAluno) + ". Sua nota final foi: %.2f " % ma)

if ma > 9:
    print("Aprovado! no conceito A")
elif ma >= 7.5:
    print("Aprovado! no conceito B")
elif ma >= 6.5:
    print("Aprovado! no conceito C")
elif ma >= 4.0:
    print("Reprovado! no conceito D")
else:
    print("Reprovado! no conceito D")
