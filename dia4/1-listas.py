dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
dias.append("Sabado")
dias.append("Domingo")

dias.pop(2)  # Elimina "Miercoles"
del dias[0:2]  # Elimina "Lunes"

dias[0] = "Lunes"
for dia in dias:
    print(dia)

