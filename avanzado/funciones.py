""" # uso de lamba y map
from functools import reduce

numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

# uso de filter 

numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(pares) 

# uso de reduce


suma = reduce(lambda x, y: x + y, numeros)
print(suma)
 """

from functools import reduce

numeros = list(range(1, 11))

dobles = list(map(lambda x: x * 2, numeros))
print("Dobles:", dobles)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

suma = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma)


# Comprensión de listas y generadores

# Listas