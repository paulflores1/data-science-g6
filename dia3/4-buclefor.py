#BUCLUE FOR

#TABLA DE MULTIPLICAR
tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))   
for contador in range(1,13,1):
    ressultado = tabla * contador
    print(f"{tabla} x {contador} = {ressultado}")