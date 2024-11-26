""" # Excepciones y manejo de errores

try:
    # Código que puede lanzar una excepción
    numero = int(input("Introduce un número: "))
except ValueError as e:
    # Código que se ejecuta si se produce una excepción
    print(f"Error: {e}. Debes introducir un número.")
else:
    # Código que se ejecuta si no se produce una excepción
    print(f"Has introducido el número {numero}.")
finally:
    # Código que se ejecuta siempre
    print("Fin del programa.") """


""" class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)

try:
   numero = int(input("Introduce un número: "))
   resultado = 10 / numero
   print(f"El resultado de la división es {resultado}.")
except ValueError as e:
    print(f"Error: {e}. Debes introducir un número.")
except ZeroDivisionError as e:
    print(f"Error: {e}. No se puede dividir por cero.")  """

try:
    num = int(input("Introduce un número: "))
except ValueError as e:
    print(f"Error: {e}. Debes introducir un número.")
else:
    print(f"Has introducido el número {num}.")
finally:
    print("Fin del programa.")