class Archivo:
    """
    Clase que simula la apertura y cierre de un archivo.
    Utiliza el constructor para inicializar el nombre del archivo y el destructor para simular su cierre.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor que inicializa el nombre del archivo.

        :param nombre_archivo: Nombre del archivo a abrir.
        """
        self.nombre_archivo = nombre_archivo
        # Simulación de apertura del archivo
        print(f"Abriendo archivo: {nombre_archivo}")

    def __del__(self):
        """
        Destructor que simula el cierre del archivo.
        Se llama automáticamente cuando el objeto es eliminado o sale del ámbito.
        """
        # Simulación de cierre del archivo
        print(f"Cerrando archivo: {self.nombre_archivo}")

    def leer_contenido(self):
        """
        Método que simula la lectura del contenido del archivo.
        """
        print(f"Leyendo contenido de {self.nombre_archivo}...")
        # Simulación de lectura (en realidad no lee nada)
        return "Contenido del archivo"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto Archivo
    archivo = Archivo("example.txt")

    # Leer el contenido del archivo
    contenido = archivo.leer_contenido()
    print(contenido)

    # El destructor se llama automáticamente cuando el objeto sale del ámbito
    # Sin embargo, para demostrar su uso explícito, podemos eliminar el objeto
    del archivo

    # Si no usamos 'del', el destructor se llamará al final del programa
    # Pero es más claro verlo explícitamente para fines educativos
