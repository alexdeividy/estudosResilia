def previsaoRodagem(gasolina, media):
    estimativa = gasolina * media
    return str(print("Estimamos que você consiga rodar por mais: %.3f " % estimativa + "KM"))


gasolinaAtual = float(input("Digite a quantidade de gasolina atual no seu veículo: "))
mediaPorKm = float(input("Digite a media de KM por litro do seu veículo: "))
previsaoRodagem(gasolinaAtual, mediaPorKm)
