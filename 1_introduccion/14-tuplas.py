#tuplas

# Las tuplas son una colección de elementos ordenados que no pueden ser modificados.
# Las tuplas son inmutables, lo que significa que no puedes cambiar, agregar o eliminar elementos una vez que se haya definido.
# Las tuplas se definen utilizando paréntesis ().

lenguajes = ("Python", "Java", "JavaScript", "C++", "C#")
print(lenguajes[1]) # Java
# print(lenguajes[1] = "Ruby") # TypeError: 'tuple' object does not support item assignment
print(lenguajes[1:]) # JavaScript
print(lenguajes[-1]) # Python
print(lenguajes[:]) # C++

edad_perro = float(input("Ingrese la edad del perro: ")) 
edad_humana = 0