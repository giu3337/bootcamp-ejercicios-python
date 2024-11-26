# Comprensión de listas y generadores

# Listas

cuadrados = [x**2 for x in range (10)]

#Generadores
def contador(n):
    for i in range(n):
        yield i

gen = contador(10)
for valor in gen:
    print(valor)