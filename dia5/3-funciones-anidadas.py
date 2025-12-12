def operacion(a,b):
    def sumar():
        return a + b

    def restar():
        return a - b

    def multiplicar():
        return a * b

    def dividir():
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"

    print("Resultados de las operaciones:")
    print(f"Suma: {sumar()}")
    print(f"Resta: {restar()}")
    print(f"Multiplicación: {multiplicar()}")
    print(f"División: {dividir()}")

operacion(10, 5)













