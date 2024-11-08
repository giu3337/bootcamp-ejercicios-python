#encapsulacion
#Es la protección de los atributos de una clase para que no puedan ser modificados desde fuera de la clase


class CuentaBancaria:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo  # atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f'Se han depositado {cantidad} en la cuenta de {self.nombre}')

    def retirar(self, cantidad):
        self.__saldo -= cantidad

    def __str__(self):
        return f'La cuenta de {self.nombre} tiene un saldo de {self.__saldo}'


# Crear una instancia de CuentaBancaria
cuenta1 = CuentaBancaria('Juan', 1000)
cuenta1.depositar(500)  # Llamar al método depositar en la instancia
print(cuenta1)  # Esto llamará a __str__ automáticamente