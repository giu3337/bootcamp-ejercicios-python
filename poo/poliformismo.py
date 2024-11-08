#polimorfismo
#Es la capacidad de un objeto de comportarse de varias formas
#El polimorfismo se logra sobreescribiendo los metodos de la clase padre en la clase hija
#En el ejemplo anterior, el metodo hablar() de la clase padre Animal se sobreescribe en las clases hijas Perro y Gato

class Deporte:
    def jugar(self):
        pass

class Futbol(Deporte):
    def jugar(self):
        print('Jugando futbol')

class Tenis(Deporte):
    def jugar(self):
        print('Jugando Tenis')

class Volley(Deporte):
    def jugar(self):
        print('Jugando Volley')


deporte1 = Futbol()
deporte1.jugar()
deporte2 = Tenis()
deporte2.jugar()
deporte3 = Volley()
deporte3.jugar()

#En este ejemplo, la clase Deporte tiene un metodo jugar() que se sobreescribe en las clases hijas Futbol, Tenis y Volley
#El metodo jugar() de la clase padre Deporte se comporta de diferentes formas en las clases hijas
#Esto es polimorfismo