class ClimaSemanal:
    def __init__(self):
        self.__temperaturas = []  # Atributo privado para almacenar temperaturas

    # Método para ingresar temperaturas diarias
    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas diarias de la semana:")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.__temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.__temperaturas:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    # Método para mostrar el promedio semanal
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")


# Programa principal
def main_poo():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()


# Ejecutar el programa orientado a objetos
print("\n**Programación Orientada a Objetos**")
main_poo()
