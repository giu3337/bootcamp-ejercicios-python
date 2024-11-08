# POO = Programación Orientada a Objetos

# CLASE = Plantilla para crear objetos

# Atributos = Características del objeto
# Métodos = Funciones del objeto (acciones)
# Self = Hace referencia al propio objeto
# __init__ = Método constructor
# __str__ = Método especial para mostrar los atributos de la clase
# Instanciar una clase = Crear un objeto de una clase


class Coche:
    def __init__(self, marca, modelo, color): # Método constructor
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self): # Método
        print(f"El coche {self.marca} {self.modelo} de color {self.color } está acelerando")

    def frenar(self): # Método 
        print(f"El coche {self.marca} {self.modelo} de color {self.color } está frenando")

    def __str__(self): # Método # Método especial para mostrar los atributos de la clase
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"
    
coche = Coche("Ferrari", "Aventador", "Rojo")

coche.acelerar()

#SELF = Hace referencia al propio objeto

       
        