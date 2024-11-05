#POO

# 1. Clases y Objetos
# 2. Atributos y Métodos
# 3. Constructores
# 4. Herencia
# 5. Encapsulamiento
# 6. Polimorfismo

# 1. Clases y Objetos
# Las clases son plantillas que nos permiten crear objetos. Los objetos son instancias de una clase.
# Las clases nos permiten definir la estructura y el comportamiento de los objetos.
# Para definir una clase en Python utilizamos la palabra reservada class seguida del
# nombre de la clase y dos puntos.

# Clases Definidas Anteriormente
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, carnet, carrera):
        super().__init__(nombre, edad, sexo)
        self.carnet = carnet
        self.carrera = carrera

    def __str__(self):
        return f"Estudiante: {self.nombre}, Carnet: {self.carnet}, Carrera: {self.carrera}"

class Profesor(Persona):
    def __init__(self, nombre, edad, sexo, codigo, especialidad):
        super().__init__(nombre, edad, sexo)
        self.codigo = codigo
        self.especialidad = especialidad

    def __str__(self):
        return f"Profesor: {self.nombre}, Código: {self.codigo}, Especialidad: {self.especialidad}"

class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def __str__(self):
        return f"Curso: {self.nombre}, Código: {self.codigo}, Profesor: {self.profesor.nombre}"

class Universidad:
    def __init__(self, nombre, cursos):
        self.nombre = nombre
        self.cursos = cursos

    def __str__(self):
        info = f"Universidad: {self.nombre}\n"
        for curso in self.cursos:
            info += f"{curso}\n"
        return info

# Crear Estudiantes
estudiante = Estudiante('Carlos Perez', 20, "m", '202010101', 'Ingeniería en Sistemas')

# Crear Profesores
mi_profesor = Profesor('Juan Perez', 40, 'M', 'P001', 'Matemáticas')
mi_profesor_2 = Profesor('Maria Lopez', 35, 'F', 'P002', 'Física')
mi_profesor_3 = Profesor('Pedro Ramirez', 45, 'M', 'P003', 'Química')
profesor = Profesor('Juan Perez', 40, 'M', 'P001', 'Matemáticas')

# Crear Cursos
curso1 = Curso('Matemáticas', 'MAT101', mi_profesor)
curso2 = Curso('Fisica', 'FIS101', mi_profesor_2)
curso3 = Curso('Quimica', 'QUI101', mi_profesor_3)

# Crear la Universidad con una única lista de cursos
universidad = Universidad('Universidad de El Salvador', [curso1, curso2, curso3])



# Imprimir la Universidad
print(estudiante)
