# POO PERSONa

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")
    
    def descripcion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

persona1 = Persona("Juan", 30)
print(persona1.nombre)
print(persona1.edad)
print(persona1.saludar())

persona2 = Persona("María", 25)

print(persona2.nombre)
print(persona2.edad)
print(persona2.saludar())