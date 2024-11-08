# Crea la clase Persona con los atributos nombre edad y profesion
# Crear 2 metodos saludar y despedirse 
# Creat 2 instancias de la clase persona y mostrar el nombre y el metodo saludar

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años y soy {self.profesion}")
    
    def despedirse(self):
        print(f"Adios, me llamo {self.nombre} y tengo {self.edad} años y soy {self.profesion}")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Profesion: {self.profesion}"
    
    def __del__(self):
        print(f"El objeto {self.nombre} ha sido eliminado")

persona1 = Persona("Juan", 30, "Ingeniero")
print(persona1.nombre)
print(persona1.edad)
print(persona1.profesion)
print(persona1.saludar())
print(persona1.despedirse())

persona2 = Persona("María", 25, "Doctora")
print(persona2.nombre)
print(persona2.edad)
print(persona2.profesion)
print(persona2.saludar())