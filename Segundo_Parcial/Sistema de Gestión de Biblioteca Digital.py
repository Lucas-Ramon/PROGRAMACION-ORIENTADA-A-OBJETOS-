class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Usaremos una tupla para el autor y título
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', user_id='{self.user_id}', libros_prestados={self.libros_prestados})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto para IDs de usuario únicos

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, nombre, user_id):
        if user_id not in [usuario.user_id for usuario in self.usuarios]:
            nuevo_usuario = Usuario(nombre, user_id)
            self.usuarios.add(nuevo_usuario)
            print(f"Usuario '{nombre}' registrado con ID {user_id}.")
        else:
            print(f"El ID de usuario {user_id} ya está registrado.")

    def dar_baja_usuario(self, user_id):
        usuario_a_eliminar = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario_a_eliminar:
            self.usuarios.remove(usuario_a_eliminar)
            print(f"Usuario con ID {user_id} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {user_id}.")

    def prestar_libro(self, isbn, user_id):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)

        if libro and usuario:
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]  # Eliminar el libro de la biblioteca
            print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
        else:
            print("No se pudo realizar el préstamo. Verifique el ISBN del libro o el ID del usuario.")

    def devolver_libro(self, isbn, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)

        if usuario:
            libro_a_devolver = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
            if libro_a_devolver:
                usuario.libros_prestados.remove(libro_a_devolver)
                self.añadir_libro(libro_a_devolver)  # Devolver el libro a la biblioteca
                print(f"Libro '{libro_a_devolver.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print("El libro no está en los libros prestados por el usuario.")
        else:
            print("No se encontró el usuario con ese ID.")

    def buscar_libro(self, criterio):
        resultados = [libro for libro in self.libros.values() if criterio.lower() in libro.titulo.lower() or
                      criterio.lower() in libro.autor.lower() or
                      criterio.lower() in libro.categoria.lower()]

        return resultados

    def listar_libros_prestados(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)

        if usuario:
            return usuario.libros_prestados
        else:
            print("No se encontró el usuario con ese ID.")
            return []


# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.añadir_libro(Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "123456789"))
biblioteca.registrar_usuario("Juan Pérez", "001")
biblioteca.prestar_libro("123456789", "001")
print(biblioteca.listar_libros_prestados("001"))
