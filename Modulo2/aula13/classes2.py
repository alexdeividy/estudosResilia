class Motor():
    def __init__(self, tipo):
        self.tipo = tipo
    
class Carro():
    def __init__(self, marca, modelo, tipoMotor):
        self.marca = marca
        self.modelo = modelo
        self.motor = tipoMotor

#Exemplo de uso
motor = Motor("V8")
carro = Carro("Fiat", "Palio", motor.tipo)
#carro = Carro("Fiat", "Palio", "V7")

#print(carro.motor.tipo) # Saida: V8
print(carro.marca) # Saida: Fiat
print(carro.motor)