#FUNCIONES EN PYTHON
#
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Las funciones ayudan a organizar el código, mejorar la legibilidad y evitar la duplicación.   

def saludar(nombre):
    mensaje = f"Hola, {nombre}! Bienvenido a Python."
    return mensaje

def sumar(a, b):
    return a + b

#lista arg
def sumar(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    return total

total = sumar(1, 2, 3, 4, 5,6,7,8,9,10)

print(f"La suma es: {total}")

#kwargs
def calculadora(**kwargs):
    print(kwargs)
    if kwargs["operacion"] == "sumar":
        return kwargs["a"] + kwargs["b"]
    elif kwargs["operacion"] == "restar":
        return kwargs["a"] - kwargs["b"]
    elif kwargs["operacion"] == "multiplicar":
        return kwargs["a"] * kwargs["b"]
    elif kwargs["operacion"] == "dividir":
        return kwargs["a"] / kwargs["b"]
resultado1 = calculadora(operacion="sumar", a=10, b=5)
resultado2 = calculadora(operacion="restar", a=10, b=5)
resultado3 = calculadora(operacion="multiplicar", a=10, b=5)
resultado4 = calculadora(operacion="dividir", a=10, b=5)

print(f"Resultado de la suma: {resultado1}")
print(f"Resultado de la resta: {resultado2}")
print(f"Resultado de la multiplicacion: {resultado3}")
print(f"Resultado de la division: {resultado4}")

sumar2 = lambda x, y: x + y

print(f"La suma con lambda es: {sumar2(5, 7)}")