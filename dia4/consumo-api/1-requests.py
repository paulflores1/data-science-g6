import requests
from  tabulate import tabulate

import mysql.connector

URL ='https://randomuser.me/api/?nat=es&results=100'





response = requests.get(URL)

if response.status_code ==200:
    print("Conexion a api exitosa")
    data = response.json()
    rows =[]
    for user in data['results']:
        nombre =f"{user['name']['first']} {user['name']['last']}"
        pais = user['location']['country']
        email = user['email']
        telefono = user['phone']
        foto = user['picture']['large']


        rows.append([nombre,pais,email,telefono,foto])

    headers =["Nombre","Pais","email","telefono","foto"]
    print(tabulate(rows,headers))

    #guardar data en base de datos
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password = 'root',
    database="db_g6")
    if connection.is_connected():
        cursor = connection.cursor(
            
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuario(
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(255) NOT NULL,
            pais VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            telefono VARCHAR(100),
            foto TEXT
            );
            """
        )
        for usuario in rows:
            cursor.execute(
                """
                insert into usuario(nombre,pais,email,telefono,foto)
                values(%s,%s,%s,%s,%s)
                """,
                usuario
            )
        connection.commit()
        connection.close()
        print("registros importados a la  base de datos")
else:
    print(f"Error{response.status_code}")