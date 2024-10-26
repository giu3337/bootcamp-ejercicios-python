
nombre = "Giuseppe"
edad = 34
ciudad = "Santiago"

mensaje = f"mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}"
# f es para formatear el string con las variables

# Los tipos de Datos en Python
# String
# Integer
# Float
# Boolean
# List
# Tuple
# Dictionary


#Listas [] (mutable)
# Una lista es una colección de elementos en un orden particular
# Se puede acceder a los elementos de una lista mediante su índice
# El índice de la lista comienza en 0
# ejemplo de lista
colores = ["rojo", "verde", "azul", "amarillo"]

#tuple () (inmutable)
# Una tupla es una colección de elementos ordenados pero no se puede modificar  (inmutable)
# ejemplo de tupla
paises = ("Chile", "Argentina", "Perú", "Bolivia")

#diferencia entre listas y tuplas
# Las listas son mutables, es decir, se pueden 
# modificar después de su creación y las tuplas son inmutables, es decir, no se pueden modificar después de su creación.

#Dictionary {}
# Un diccionario es una colección de elementos que se almacenan en pares clave-valor
# ejemplo de diccionario
persona = {
    "nombre": "Giuseppe",
    "edad": 34,
    "ciudad": "Santiago"
}

#range() start, stop y step
# La función range() se utiliza para generar una secuencia de números
# ejemplo de range
numeross = range(1,10,2) # del 1 al 10 de 2 en 2

#actividad 1

numeros = [1,2,3,4,5,6,7,8,9,10] # lista
colores = ("rojo", "verde", "azul", "amarillo")     # tupla
user = {
    "nombre": "Giuseppe",
    "edad": 34,
    "ciudad": "Quito"
} # diccionario

es_mayor_de_edad = True # boolean

# ¿Qué tipo de datos es la variable numeros[0]? ¿Y la variable colores[1]? ¿Y la variable persona[“nombre”]? ¿Y la variable es_mayor_de_edad?
# numeros[0] es un integer
# colores[1] es un string
# persona["nombre"] es un string
# es_mayor_de_edad es un boolean




# numeros[0:5]? # [1, 2, 3, 4, 5]
# colores[1:]? # ['verde', 'azul', 'amarillo']

#control de flujo

# if, elif, else
# if se usa para evaluar una condición


# if y condicionales
# if se usa para evaluar una condición
# elif se usa para evaluar múltiples condiciones
# else se usa para ejecutar un bloque de código si la condición es falsa
# if condicion:
    # Bloque de código si la condición es verdadera


"""
edad = 18 
if edad < 18: 
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18")
else:
    print("Eres mayor de edad")"""

#operadores de comparación
# == igual
# != diferente
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que

#operadores lógicos
# and y
# or o
# not no


edad = 18

if edad >= 18 and edad <= 30:
    print("Eres un joven adulto")

# While loop

# Un bucle while se utiliza para ejecutar un bloque de código mientras la condición sea verdadera

# while condicion:
    # Bloque de código

# ejemplo de while loop
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Diferencia entre while y for loop
# Un bucle for se utiliza para iterar sobre una secuencia de elementos
# Un bucle while se utiliza para ejecutar un bloque de código mientras la condición sea verdadera

