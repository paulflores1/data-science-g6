from prefect import task
import requests
@task
def extract_data():
    """Extraer datos de ramdom users"""

    URL = 'https://randomuser.me/api/?results=20'
    response = requests.get(URL)
    if response.status_code == 200:
        extract_data = response.json()["results"]
    return extract_data
