#BUCLE WHILE
contador = 1
tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))  
while contador <= 12:
     
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")
    contador += 1