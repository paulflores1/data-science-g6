#CALCULADORA
# Programa que simula una calculadora básica
#ENTRADA DE DATOS
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion (+, -, *, /): ")

#PROCESO DE DATOS

if operacion == "+":
    resultado = numero1 + numero2
    
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Error: Division por cero no es permitida.")
        exit()

else:
    print("Operacion no valida")
    exit()
    
#SALIDA DE DATOS
print(f" {numero1} {operacion} {numero2} es: {resultado}")