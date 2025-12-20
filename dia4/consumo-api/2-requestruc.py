import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_URL = 'https://apiperu.dev/api/ruc'
API_TOKEN = os.getenv("TOKEN")
RUC = "20117592899"

DATA_REQUEST = {
    "ruc":RUC
}

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL,json=DATA_REQUEST,headers=headers)

if response.status_code == 200:
    data = response.json()['data']
    print("="*50)
    print(f'RUC : {data['ruc']}')
    print(f'Razon Social : {data["nombre_o_razon_social"]}')
    print(f'Dirección : {data["direccion"]}')
    print(f'Distrito : {data["distrito"]}')
    print(f'Provincia : {data["provincia"]}')
    print(f'Departamento : {data["departamento"]}')
    print(f'ubigeo : {data["ubigeo_sunat"]}')
else:
    print("error en la solicitud de datos")