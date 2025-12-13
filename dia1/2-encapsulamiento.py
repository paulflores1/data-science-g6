#ENCAPSULAMIENTO
class Usuario:

    __email = "admin@admin.com" # DOS GUIONES BAJOS ANTES DE LA VARIABLE LA VUELVE PRIVADA
    __password = "admin123" # DOS GUIONES BAJOS ANTES DE LA VARIABLE LA VUELVE PRIVADA

    def __init__(self):
     pass

    def login(self, email, password):
        if email == self.__email and password == self.__password:
            print("Login exitoso")
        else:
            print("Login fallido")


print("LOGIN USUARIO")
email_input = input("Ingrese su email: ")
password_input = input("Ingrese su password: ")
Usuario = Usuario()
print(Usuario.__password)
Usuario.login(email_input, password_input)
    