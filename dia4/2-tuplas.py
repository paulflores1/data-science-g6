#las tuplas son immutables
dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
print(f"Tipo de dato original: {type(dias)}")
dias = list(dias)  # Convertimos la tupla a lista para poder modificarla

print(f"Tipo de dato despues de la conversion: {type(dias)}")

dias.append("sabado")  # Esto generará un error
print(dias)