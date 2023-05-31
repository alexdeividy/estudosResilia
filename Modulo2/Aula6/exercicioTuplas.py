TuplaNomes = ("Alex", "Vanderlei", "Aron", "Gabriel",)

def saudacoes(nome):
    for nome in TuplaNomes:
        print("Saudacoes!", nome)
    print("-"*20)

saudacoes(0)
print(len(TuplaNomes))

TuplaNomes = TuplaNomes + ("Rafael",)

saudacoes(0)
print(len(TuplaNomes))

TuplaNomes[0] = "Rafael"
TuplaNomes.pop(0)
TuplaNomes.append("Rafael")