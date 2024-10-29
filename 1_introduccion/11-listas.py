# listas 

lenguajes = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
print(lenguajes[0]) # Python
print(lenguajes[1]) # Java
print(lenguajes[2]) # C++
print(lenguajes[3]) # C#
print(lenguajes[4]) # JavaScript

lenguajes[1] = 'Ruby' # Cambiar el valor de un elemento
print(lenguajes[1:4]) # ['Ruby', 'C++', 'C#']  
#[1:4] significa que se imprimiran los elementos desde el indice 1 hasta el indice 4
print(lenguajes[:3]) # ['Python', 'Ruby', 'C++']
# [:3] significa que se imprimiran los elementos desde el principio hasta el indice 3
print(lenguajes[2:]) # ['C++', 'C#', 'JavaScript']
# [2:] significa que se imprimiran los elementos desde el indice 2 hasta el final
print(lenguajes[-1]) # JavaScript
# [-1] significa que se imprimirá el último elemento
print(lenguajes[-2]) # C#
# [-2] significa que se imprimirá el penúltimo elemento

# Metodos de las listas
# append() agrega un elemento al final de la lista
# insert() agrega un elemento en un indice especifico
lenguajes.insert(2, 'PHP') # ['Python', 'Ruby', 'PHP', 'C++', 'C#', 'JavaScript'] # PHP se agrega en el indice 2
# remove() remueve un elemento de la lista
lenguajes.remove('PHP') # ['Python', 'Ruby', 'C++', 'C#', 'JavaScript'] # PHP se remueve de la lista
# pop() remueve un elemento de la lista por su indice
# clear() remueve todos los elementos de la lista
# sort() ordena los elementos de la lista
# reverse() invierte el orden de los elementos de la lista
# copy() devuelve una copia de la lista
# count() devuelve el numero de veces que aparece un elemento en la lista
# index() devuelve el indice de un elemento en la lista
# extend() agrega los elementos de una lista a otra lista
# copy() devuelve una copia de la lista
# len() devuelve el numero de elementos
print(len(lenguajes)) # 5


print("Python" in lenguajes) # True
# in se utiliza para verificar si un elemento esta en la lista