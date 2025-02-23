class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe en el inventario.")
        else:
            self.productos.append(producto)
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]
        print("Producto eliminado (si existía).")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados if encontrados else "No se encontraron productos."

    def mostrar_inventario(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Ingrese nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if isinstance(resultados, list):
                for p in resultados:
                    print(p)
            else:
                print(resultados)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
