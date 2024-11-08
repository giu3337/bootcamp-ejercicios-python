# POO ANIMAL

class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie


    def descripcion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}")

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def __del__(self):
        print(f"El objeto {self.nombre} ha sido eliminado")

gato = Animal("Tom", 3, "Felino")
gato.descripcion()
gato.comer()

#del gato # Elimina el objeto gato
        