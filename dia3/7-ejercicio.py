#CALCULADORA BANDERA
# INCLUYE CONVERSION DE MONEDAS
print("\033[H\033[J", end="")
salir = "no"
while salir =="no":
    
    #ENTRADA DE DATOS
    print("============CALCULADORA BASICA============")
    
    print("============OPERACIONES============")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicacion (*)")  
    print("4. Division (/)")
    print("5. tabla de multiplicar")
    print("6. Convertir Soles a Dolares")
    print("7. Convertir Dolares a Soles")
    print("===================================")

    opcion = int (input("Ingrese la opcion: "))
    
#PROCESO DE DATOS
    if opcion == 5:
        tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))   
        for contador in range(1,13,1):
            ressultado = tabla * contador
            print(f"{tabla} x {contador} = {ressultado}")

    elif opcion >=1 and opcion <=4:
            numero1 = int(input("Ingrese el primer numero: "))
            numero2 = int(input("Ingrese el segundo numero: "))
            if opcion == 1:
                resultado = numero1 + numero2
                tipo = "+"
            elif opcion == 2:
                resultado = numero1 - numero2
                tipo = "-"
            elif opcion ==3:
                resultado = numero1 * numero2
                tipo = "*"
            elif opcion == 4:
                if numero2 != 0:
                    resultado = numero1 / numero2
                    tipo = "/"
                else:
                    print("Error: Division por cero no es permitida.")
                    exit()

            else:
                print("Operacion no valida")
                
                
            #SALIDA DE DATOS
            print(f" {numero1} {tipo} {numero2} es: {resultado}")       
    elif opcion == 6:
        soles = float(input("Ingrese la cantidad en Soles: "))
        tasa_cambio =3  # Ejemplo de tasa de cambio
        dolares = soles / tasa_cambio
        print(f"S/. {soles:,.2f}   son $ {dolares:,.2f} ")
    elif opcion == 7:
        dolares = float(input("Ingrese la cantidad en Dolares: "))
        tasa_cambio =3  # Ejemplo de tasa de cambio
        soles = dolares * tasa_cambio
        print(f"$ {dolares:,.2f}    son S/. {soles:,.2f} ")

    salir = input("Desea salir de la calculadora (si/no): ")
    if salir == "si":
        print("Gracias por usar la calculadora")
        break
        