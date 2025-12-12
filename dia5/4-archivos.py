#escribir archivo

with open("archivo.txt", "a") as archivo:
    nueva_linea = "Ana Gomez"
    archivo.write("\n")
    archivo.write(nueva_linea)
    
with open("archivo.txt", "w") as archivo:
    archivo.write("Paul Vizcarra Flores\n")
    archivo.write("Carlos Perez\n")
#leer archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(f"Línea: {linea.strip()}")

#agregar contenido al archivo









































































