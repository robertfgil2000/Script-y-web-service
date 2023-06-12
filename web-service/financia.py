import yfinance as yf
from flask import Flask, request, jsonify
from datetime import date
import sys

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_stock_value():
    data = request.get_json()

    # Obtener los datos de la solicitud
    accion = data['accion']
    fecha_inicial = data['fecha_inicial']
    fecha_final = data['fecha_final']

    # Realizar la consulta a yfinance para obtener los datos de la acción   
    valores = yf.download(accion, fecha_inicial, fecha_final)
    valores.index = valores.index.strftime('%Y-%m-%d %H:%M:%S')

    # Crear la respuesta en formato JSON con el valor consolidado
    
    # Devolver la respuesta en formato JSON
    return jsonify(valores.to_dict())

if __name__ == '__main__':
    app.debug=True
    app.run()
