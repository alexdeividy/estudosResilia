class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * self.base + self.altura

retangulo1 = Retangulo(10, 10)
retangulo1.area()
retangulo1.perimetro()

print(f"A área do retângulo é de:{retangulo1.area()}, e o perimetro é:{retangulo1.perimetro()}")