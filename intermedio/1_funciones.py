#funciones en python

#Una función es un bloque de código que solo se ejecuta cuando se llama.
#Puedes pasar datos, conocidos como parámetros, a una función.



def nombre_funcion(): 
    print("Hola mundo")

nombre_funcion() # Hola mundo

def saludar(nombre):
    return (f"Hola {nombre}")

saludar("Giuseppe") # Hola Giusseppe

llamar = saludar("Giuseppe")