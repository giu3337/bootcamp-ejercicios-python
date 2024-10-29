# if 

""" puntaje = 9.8 
if puntaje >= 9.5:
    print("Excelente")
elif puntaje >= 8.5:
    print("Muy bien")
elif puntaje >= 7.5:
    print("Bien")
else:
    print("Regular")

edad = int(input("Ingrese su edad: ")) 
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad") """


# Este codigo convierte una temperatura de grados Celsius a Fahrenheit
# y viceversa

temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad de temperatura (C o F): ")
if unidad == "C":
    fahrenheit = (temperatura * 9/5) + 32
    print(f"{temperatura} grados Celsius son {fahrenheit} grados Fahrenheit")
elif unidad == "F":
    celsius = (temperatura - 32) * 5/9
    print(f"{temperatura} grados Fahrenheit son {celsius} grados Celsius")
else:
    print("Unidad de temperatura no valida")


