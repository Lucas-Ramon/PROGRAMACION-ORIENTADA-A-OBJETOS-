class Bicicleta:
    """Clase que representa una bicicleta."""

    def __init__(self, id_bicicleta, modelo):
        self.id_bicicleta = id_bicicleta  # Identificador único de la bicicleta
        self.modelo = modelo  # Modelo de la bicicleta
        self.disponible = True  # Estado de disponibilidad de la bicicleta

    def alquilar(self):
        """Marca la bicicleta como no disponible."""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        """Marca la bicicleta como disponible."""
        self.disponible = True


class Usuario:
    """Clase que representa un usuario del sistema."""

    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del usuario
        self.reservas = []  # Lista de reservas del usuario

    def hacer_reserva(self, reserva):
        """Agrega una reserva a la lista del usuario."""
        self.reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        """Cancela una reserva del usuario."""
        if reserva in self.reservas:
            self.reservas.remove(reserva)
            reserva.bicicleta.devolver()  # Devolver la bicicleta al inventario


class Reserva:
    """Clase que representa una reserva de bicicleta."""

    def __init__(self, bicicleta, usuario):
        self.bicicleta = bicicleta  # Bicicleta reservada
        self.usuario = usuario  # Usuario que realiza la reserva

    def __str__(self):
        return f'Reserva de {self.usuario.nombre} para la bicicleta {self.bicicleta.modelo}'


class SistemaDeReservas:
    """Clase que gestiona el sistema de reservas."""

    def __init__(self):
        self.bicicletas = []  # Lista de bicicletas disponibles
        self.usuarios = []  # Lista de usuarios registrados

    def agregar_bicicleta(self, bicicleta):
        """Agrega una nueva bicicleta al sistema."""
        self.bicicletas.append(bicicleta)

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en el sistema."""
        self.usuarios.append(usuario)

    def reservar_bicicleta(self, id_bicicleta, usuario):
        """Realiza una reserva si la bicicleta está disponible."""
        for bici in self.bicicletas:
            if bici.id_bicicleta == id_bicicleta and bici.alquilar():
                nueva_reserva = Reserva(bici, usuario)
                usuario.hacer_reserva(nueva_reserva)
                print(f'Bicicleta {bici.modelo} reservada por {usuario.nombre}.')
                return nueva_reserva
        print('Bicicleta no disponible para reservar.')
        return None

# Ejemplo de uso del sistema
if __name__ == "__main__":
    sistema = SistemaDeReservas()

    # Agregar bicicletas al sistema
    bici1 = Bicicleta(1, "Bici Montaña")
    bici2 = Bicicleta(2, "Bici Ruta")
    sistema.agregar_bicicleta(bici1)
    sistema.agregar_bicicleta(bici2)

    # Registrar usuarios
    usuario1 = Usuario("Alice")
    sistema.registrar_usuario(usuario1)

    # Realizar reservas
    reserva1 = sistema.reservar_bicicleta(1, usuario1)  # Reserva exitosa
    reserva2 = sistema.reservar_bicicleta(1, usuario1)  # Reserva fallida (no disponible)

    # Cancelar reserva
    if reserva1:
        usuario1.cancelar_reserva(reserva1)
        print(f'Reserva cancelada: {reserva1}')
