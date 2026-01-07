from tasks.extract import extract_data
from tasks.transform import transform_data
from tasks.load import load
from prefect import flow
from tabulate import tabulate
@flow
def main_flow():
    data = extract_data()
    transformed_data =  transform_data(data)
    cabeceras = ["Nombre", "Sexo", "Pais", "Fecha Nacimiento"]
    print(tabulate(transformed_data, headers=cabeceras, tablefmt="grid"))
    load(transformed_data)
    resultado = load(transformed_data)
    print(f"Se han insertado {resultado} registros en la base de datos.")

if __name__ == "__main__":
    main_flow()