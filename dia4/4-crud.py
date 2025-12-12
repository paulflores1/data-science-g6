import os
from time import sleep 


dic_alumnos = {
    "1234567": {"nombre": "Juan Perez", "email": "juanperez@gmail.com"},
    }
ancho_menu = 50
while True:
    os.system("clear")
    print(" " *10 + "GESTION DE ALUMNOS")
    print("-" * ancho_menu)
    print("""
            [1]. REGISTAR ALUMNO
            [2]. MOSTRAR ALUMNOS
            [3]. ACTUALIZAR ALUMNOS
            [4]. ELIMINAR ALUMNO
            [5]. SALIR
          """
          )
    print("-" * ancho_menu)
    opcion = input("Seleccione una opcion [1-5]: ")
    os.system("clear")
    if opcion == "1":
        print("=" * ancho_menu)
        print(" " *10 + "REGISTRO DE ALUMNO")
        print("=" * ancho_menu)
        dni = input("Ingrese DNI: ")
        if not dni in dic_alumnos:
            nombre = input("Ingrese Nombre: ")
            email = input("Ingrese Email: ")
            dic_alumnos[dni] = {"nombre": nombre, "email": email}
            print(f"Alumno {nombre} registrado exitosamente.")
        else:
            print("El alumno ya se encuentra registrado.")


    elif opcion == "2":
        print("=" * ancho_menu)
        print(" " *10 + "MOSTRAR ALUMNOS")
        print("=" * ancho_menu)
        for dni, info in dic_alumnos.items():
            print(f"DNI: {dni}")
            print(f"Nombre: {info['nombre']}")
            print(f"Email: {info['email']}")
            print("-" * ancho_menu)

    elif opcion == "3":
        print("=" * ancho_menu)
        print(" " *10 + "ACTUALIZAR ALUMNO")
        print("=" * ancho_menu)
        dni = input("Ingrese DNI del alumno a actualizar: ")
        if dni in dic_alumnos:
            nuevo_nombre = input("Ingrese nuevo Nombre (ENTER para no actualizar): ")
            nuevo_email = input("Ingrese nuevo Email(ENTER para no actualizar): ")
            if nuevo_nombre:
                dic_alumnos[dni]["nombre"] = nuevo_nombre
            if nuevo_email:
                dic_alumnos[dni]["email"] = nuevo_email
            print(f"Alumno actualizado exitosamente!!!.")
        else:
            print("Alumno no encontrado.")


    elif opcion == "4":
        print("=" * ancho_menu)
        print(" " *10 + "ELIMINAR ALUMNO")
        print("=" * ancho_menu)
        ingrese_dni = input("Ingrese DNI del alumno a eliminar: ")
        if ingrese_dni in dic_alumnos:
            del dic_alumnos[ingrese_dni]
            print("Alumno eliminado exitosamente.")
        else:
            print("Alumno no encontrado.")
    elif opcion == "5":
        print("=" * ancho_menu)
        print(" " *10 + "SALIENDO DEL SISTEMA")
        print("=" * ancho_menu)
        sleep(2)
        break
    input("Presione ENTER para continuar...")   