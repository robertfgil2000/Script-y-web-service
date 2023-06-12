import requests

def get_stock_data():
    url = "http://localhost:5000/" 
    data = {
        "accion": "GOOGL",
        "fecha_inicial": "2020-01-01",
        "fecha_final": "2022-01-01"
    }

    response = requests.post(url, json=data)  # Realizar la solicitud POST

    if response.status_code == 200:  # Verificar si la solicitud fue exitosa (código de respuesta 200)
        json_data = response.json()  # Devuelve el resultado en formato JSON
        # imprimir los resultados en orden de menor a mayor
        for key, values in json_data.items():
            print(f'"{key}": {{')
            for date, value in values.items():
                print(f'  "{date}": {value},')
            print('}')
    else:
        print("Error en la solicitud:", response.status_code)

get_stock_data()  # Llamar a la función para obtener los datos del webservice
