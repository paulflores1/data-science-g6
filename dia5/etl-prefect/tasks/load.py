from prefect import task
import mysql.connector

@task
def load(data):
    resultado =0
    cn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_g6")
    cursor = cn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS random_user(
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   nombre VARCHAR(255) NOT NULL,
                   sexo VARCHAR(50) NOT NULL,
                   pais VARCHAR(255) NOT NULL,
                   fecha_nacimiento DATE NOT NULL
        );""")
    
    cn.commit()
    insert_query = """
        INSERT INTO random_user (nombre, sexo, pais, fecha_nacimiento)
        VALUES (%s, %s, %s, %s)"""
    cursor.executemany(insert_query, data)
    cn.commit()
    resultado = cursor.rowcount
    cursor.close()
    cn.close()
    return resultado