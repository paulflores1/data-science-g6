#DICCIONARIOS
#Estructura de datos que almacena pares de clave-valor
capitales = {
    "Peru": "Lima",
    "Ecuador": "Quito",
    "Colombia": "Bogota",
    "Argentina": "Buenos Aires"
}
    
#acceder a un valor mediante su clave
print(capitales["Ecuador"]) 

#agregar un nuevo par clave-valor
capitales["Chile"] = "Santiago"

nuevo_capitales = {
    "Bolivia": "La Paz"}
capitales.update(nuevo_capitales)  #agregar varios pares clave-valor
#eliminar un par clave-valor
del capitales["Argentina"]
capital_eliminada = capitales.pop("sdf","No existe")  #elimina y devuelve el valor asociado a la clave
print(f" capital eliminada {capital_eliminada}")
print(capitales)
print("-----")
#iterar sobre las claves y valores del diccionario
for clave in capitales.keys():
    print(f"Pais: {clave}")
print("-----")
for valor in capitales.values():
    print(f"Capital: {valor}")
print("-----")
for pais, ciudad in capitales.items():
    print(f"La capital de {pais} es {ciudad}")
