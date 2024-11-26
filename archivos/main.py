#Escritura de archivo

with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo.")

#Lectura de archivo

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)        

 """ 
 
 Ejemplo Práctico Objetivo:

Aprender a leer y escribir archivos de texto en Python.

Descripción: Crear un programa que pida al usuario un texto y lo escriba en un archivo de texto. Luego, el programa debe leer el archivo y mostrar su contenido.

Instrucciones:

Pide un texto al usuario.

Escribe ese texto en un archivo llamado entrada.txt.

Luego, lee el archivo y muestra su contenido en la consola.

 """

