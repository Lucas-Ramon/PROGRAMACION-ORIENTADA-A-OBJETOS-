# Definición de la clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado

    # Métodos getters para acceder a los atributos privados
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    # Método para mostrar información del vehículo
    def mostrar_info(self):
        return f"Vehículo: {self.get_marca()} {self.get_modelo()}"

# Definición de la clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.__puertas = puertas  # Atributo privado

    # Método sobrescrito para mostrar información del coche
    def mostrar_info(self):
        return f"Coche: {self.get_marca()} {self.get_modelo()}, Puertas: {self.__puertas}"

# Definición de otra clase derivada
class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base

    # Método sobrescrito para mostrar información de la moto
    def mostrar_info(self):
        return f"Moto: {self.get_marca()} {self.get_modelo()}"

# Creación de instancias de las clases
mi_coche = Coche("Toyota", "Corolla", 4)
mi_moto = Moto("Yamaha", "MT-07")

# Uso de los métodos para demostrar la funcionalidad
print(mi_coche.mostrar_info())  # Demuestra el uso del método sobrescrito en Coche
print(mi_moto.mostrar_info())    # Demuestra el uso del método sobrescrito en Moto

# Ejemplo de polimorfismo: se puede usar una lista que contenga ambos tipos de vehículos
vehiculos = [mi_coche, mi_moto]
for vehiculo in vehiculos:
    print(vehiculo.mostrar_info())  # Llama al método correspondiente según el objeto
