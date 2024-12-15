class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")


# Uso
auto = Automovil("Toyota", "Corolla", 4)
auto.mostrar_info()
