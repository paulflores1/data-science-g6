import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password = 'root',
    database="db_g6")

print("Conexion exitosa a la base de datos")

cursor = connection.cursor()
cursor.execute("SELECT nombre,email FROM alumno")
resultados = cursor.fetchall()
print("=====DATOS DEL ALUMNO=====")
for fila in resultados:
    print("-"*30)
    print(f"Nombre: {fila[0]}")
    print(f"Email: {fila[1]}")

connection.close()