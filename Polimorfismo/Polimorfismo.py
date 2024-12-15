class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Uso
animales = [Perro(), Gato()]

for animal in animales:
    print(animal.hacer_sonido())
