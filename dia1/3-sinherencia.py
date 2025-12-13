class Alumno:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")

Alumno1 = Alumno("Juan Perez", "jperez@mgail.com")
Alumno1.mostrar()

class Profesor:
    def __init__(self, nombre, email, especialidad):
        self.nombre = nombre
        self.email = email
        self.especialidad = especialidad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Especialidad: {self.especialidad}")

profesor = Profesor("Ana Gomez", "agomez@gmail.com","matematicas")
profesor.mostrar()
