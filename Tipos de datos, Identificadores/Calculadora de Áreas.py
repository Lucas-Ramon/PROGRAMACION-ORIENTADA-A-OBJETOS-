# Este programa calcula el área de diferentes figuras geométricas: círculo, rectángulo y triángulo.
# Permite al usuario elegir la figura y proporciona el área correspondiente.

import math  # Importamos la biblioteca math para usar funciones matemáticas


def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * (radio ** 2)  # Fórmula del área del círculo: π * r^2
    return area


def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    area = base * altura  # Fórmula del área del rectángulo: base * altura
    return area


def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    area = (base * altura) / 2  # Fórmula del área del triángulo: (base * altura) / 2
    return area


def main():
    """Función principal que ejecuta el programa."""
    print("Calculadora de Áreas")

    # Solicitar al usuario que elija una figura
    figura = input("Elija una figura (círculo, rectángulo, triángulo): ").strip().lower()

    if figura == "círculo":
        # Solicitar el radio y calcular el área
        radio = float(input("Ingrese el radio del círculo: "))
        area_circulo = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area_circulo:.2f}")

    elif figura == "rectángulo":
        # Solicitar la base y altura y calcular el área
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area_rectangulo = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area_rectangulo:.2f}")

    elif figura == "triángulo":
        # Solicitar la base y altura y calcular el área
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area_triangulo = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area_triangulo:.2f}")

    else:
        print("Figura no válida. Por favor, elija círculo, rectángulo o triángulo.")


# Ejecutar la función principal si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()
