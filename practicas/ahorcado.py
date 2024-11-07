# Juego de Ahorcado en Python

import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "juego", "ahorcado", "computadora"]
    return random.choice(palabras)

AHORCADO_DIBUJO = [
    """
       |
       |
       |
       |
    """,
    """
       |
       |
       O
       |
    """,
    """
       |
       |
       O
      /|
    """,
    """
       |
       |
       O
      /|\\
       |
    """,
    """
       |
       |
       O
      /|\\
       |
      /
    """,
    """
       |
       |
       O
      /|\\
       |
      / \\
    """
]

print(len(AHORCADO_DIBUJO))
for etapa in AHORCADO_DIBUJO:
    print(etapa)

def mostrar_ahorcado(intentos_fallidos):
    print(AHORCADO_DIBUJO[intentos_fallidos])