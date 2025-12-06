#Creamos un programa que sume 2 numeros
#Para crear un programa dividimos el codigo en tres partes:
#1. Entrada de datos
#2. Proceso de datos
#3. Salida de datos

#1. Entrada de datos
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print("el tipo de datos de numero 1 es: ", type(numero1))
print("el tipo de datos de numero 2 es: ", type(numero2))

#2. Proceso de datos
suma = numero1 + numero2

#3. Salida de datos
print(f"La suma de los numeros es: {suma}")