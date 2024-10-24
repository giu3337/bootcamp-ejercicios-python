#Clase Uno de la clase de Python

# Terminal 
# Aprender a usar la terminal de comandos desde el comando.
# Aprender a usar Git. 


# Variables
# Variables en Python son objetos que guardan un valor.
#type() -> Función que nos permite saber el tipo de dato de una variable.

#Datos Primitivos

nombre = "Giuseppe"
numero = 34
decimal = 3.14 #float
booleano = True

#Datos Compuestos

#Listas
lista = [1,2,3,4,5] #Array
#Tuplas
tupla = (1,2,3,4,5) #Array Inmutable
#Diccionarios
diccionario = {
    "nombre": "Giuseppe",
    "edad": 34,
    "nacionalidad": "Argentino"
} #Objeto


#Strings -> Cadenas de texto

name = "Giuseppe"
last_name = "Garcia"
nombre_completo = name + " " + last_name
print(nombre_completo)
print(nombre_completo.find("G"))
# -1 -> No existe el texto

#Metodos de los Strings
#upper() -> Convierte el texto a mayusculas
#lower() -> Convierte el texto a minusculas
#capitalize() -> Convierte la primera letra en mayuscula
#strip() -> Elimina los espacios en blanco
#replace() -> Reemplaza un texto por otro
#split() -> Divide un texto en base a un caracter
#find() -> Busca un texto dentro de otro
#isnumeric() -> Devuelve True si el texto es un numero
#isalpha() -> Devuelve True si el texto es una letra

# Pedir Datos al Usuario
#input() -> Función que nos permite pedir datos al usuario
#int() -> Convierte un texto a un numero entero
#float() -> Convierte un texto a un numero decimal

age = input("Ingrese su edad: ") #string
print("Su edad es: ", age)
print(type(age))
print("Su edad sera dentro de 10 años: ", int(age) + 10) #int convertir a entero

#conversion
#str() -> Convierte un numero a un texto
#float() -> Convierte un numero entero a un numero decimal
#int() -> Convierte un numero decimal

edade = input("Ingrese su edad: ") #string
edade_convertida = int(edade)
print("Su edad es: ", edade)
edade_futura = edade_convertida + 10
print("Su edad sera dentro de 10 años: " + str(edade_futura)) #int convertir a entero
print("Su edad sera dentro de 10 años: " , edade_futura) #int convertir a entero

#Operadores Aritmeticos

# + -> Suma
print(5 + 3)  #8
# - -> Resta
print(5 - 3)  #2
# * -> Multiplicación
print(5 * 3) #15
# / -> División
print(5 / 3) #1.6666666666666667
# // -> División Entera
print(5 // 3) #1
# % -> Modulo (Resto de la división)
print(5 % 3) #2
# ** -> Potencia (Exponente)
print(5 ** 3) #125

#Operadores de Comparación

# == -> Igualdad
print(5 == 5) #True
# != -> Diferencia
print(5 != 5) #False
# > -> Mayor que
print(5 > 3) #True
# < -> Menor que
print(5 < 3) #False
# >= -> Mayor o igual que
print(5 >= 5) #True
# <= -> Menor o igual que
print(5 <= 3) #False

#Operadores logicos

# and -> Y
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False
# or -> O
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False
# not -> Negación
print(not True) #False
print(not False) #True

# And -> True si ambos son True
print(5 > 3 & 5 < 10) #True
# Or -> True si uno de los dos es True
print(5 > 3 | 5 < 10) #True
# Not -> True si el valor es False
print(not 5 > 3) #False



#Estructuras de Control

#Condicionales

