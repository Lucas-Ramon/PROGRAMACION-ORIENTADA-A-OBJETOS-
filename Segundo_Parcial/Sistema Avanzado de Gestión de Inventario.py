import pickle


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("El ID ya existe.")
        else:
            self.productos[producto.id] = producto
            self.guardar_en_archivo()
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos.")

    def mostrar_todos(self):
        if self.productos:
            for p in self.productos.values():
                print(p)
        else:
            print("Inventario vacío.")

    def guardar_en_archivo(self):
        with open("inventario.pkl", "wb") as f:
            pickle.dump(self.productos, f)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.pkl", "rb") as f:
                self.productos = pickle.load(f)
        except FileNotFoundError:
            self.productos = {}


# Menú interactivo
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_todos()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
