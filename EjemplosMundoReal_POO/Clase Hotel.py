class Hotel:
    def __init__(self, nombre, ubicacion, num_habitaciones):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.num_habitaciones = num_habitaciones
        self.habitaciones_disponibles = num_habitaciones
        self.reservas = []

    def realizar_reserva(self, reserva):
        if self.habitaciones_disponibles >= reserva.num_huespedes:
            self.reservas.append(reserva)
            self.habitaciones_disponibles -= reserva.num_huespedes
            print("Reserva realizada con éxito.")
        else:
            print("No hay suficientes habitaciones disponibles.")

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)
            self.habitaciones_disponibles += reserva.num_huespedes
            print("Reserva cancelada con éxito.")
        else:
            print("No se encontró la reserva.")

class Reserva:
    def __init__(self, fecha_entrada, fecha_salida, num_huespedes):
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.num_huespedes = num_huespedes