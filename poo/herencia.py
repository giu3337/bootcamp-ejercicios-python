# herencia de clases
# una clase puede heredar de otra clase
# la clase hija hereda los metodos y atributos de la clase padre
# la clase hija puede sobreescribir los metodos de la clase padre
# super() se usa para llamar a los metodos de la clase padre


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass # se define en las clases hijas 

    def comer(self):
        print(f'{self.nombre} esta comiendo')

    def dormir(self):
        print(f'{self.nombre} esta durmiendo')


class Perro(Animal):
    def hablar(self):
        print(f'{self.nombre} esta ladrando')

class Gato(Animal):
    def hablar(self):
        print(f'{self.nombre} esta maullando')

animal1 = Perro('Firulais')
animal2 = Gato('Garfield')

animal1.hablar()
animal2.hablar()

