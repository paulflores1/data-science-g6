class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")

class Alumno(Persona):
    def __init__(self, nombre, email,curso):
        super().__init__(nombre, email)
        self.curso = curso

    def mostrar(self):
        print("=====DATOS DEL ALUMNO=====")
        super().mostrar()
        print(f"Curso: {self.curso}")

class Profesor(Persona): #herencia de la clase Persona
    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email) #super llama al constructor de la clase padre
        self.especialidad = especialidad

    def mostrar(self):
        print("=====DATOS DEL PROFESOR=====")
        super().mostrar() #super llama al metodo mostrar de la clase padre
        print(f"Especialidad: {self.especialidad}")


Alumno1 = Alumno("Juan Perez", "jperez@mgail.com","Quimica")
Alumno1.mostrar()

Profesor1 = Profesor("Ana Gomez", "agomez.com","matematicas")
Profesor1.mostrar()
