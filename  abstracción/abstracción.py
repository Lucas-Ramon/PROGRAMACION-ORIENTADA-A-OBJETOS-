from abc import ABC, abstractmethod


class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def calcular_area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto


# Uso
figura1 = Circulo(5)
figura2 = Rectangulo(4, 7)
print(f"Área del círculo: {figura1.calcular_area()}")
print(f"Área del rectángulo: {figura2.calcular_area()}")
