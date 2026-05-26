from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
DATA_FILE = '/var/www/html/peritajes.json'

# Inventario inventado
registros = {
    "servidor": "Ubuntu de Neira",
    "hora": str(datetime.now()),
    "inventario": [
        {
            "moto": "Ford Raptor",
            "placa": "NSB308",
            "estado": "Cambio llantas"
        },
        {
            "moto": "Kawasaki FZ900",
            "placa": "NSB830",
            "estado": "Mantenimiento"
        },
        {
            "moto": "pulsar 200NS",
            "placa": "NSB832",
            "estado": "Cambio de aceite"
        }
    ]
}

# Lista de peritajes
peritajes = [
    {
        "placa": "NBS830"
    }
]

# Ruta GET inventario (Dejamos SOLO 'GET' para evitar confusiones)
@app.route('/api/registros', methods=['GET'])
def ver_registros():
    return jsonify(registros)

# Ruta GET peritajes (Para ver las placas acumuladas)
@app.route('/api/peritajes', methods=['GET'])
def ver_peritajes():
    return jsonify(peritajes)

# Ruta POST peritajes (Esta es la que procesa y guarda la nueva placa)
@app.route('/api/peritajes', methods=['POST'])
def agregar_peritaje():
    data = request.get_json()

    # Validación por si mandas el body vacío en Postman
    if not data or "placa" not in data:
        return jsonify({"error": "Falta el campo 'placa' en la petición"}), 400

    nueva_placa = {
        "placa": data["placa"].upper()
    }

    peritajes.append(nueva_placa)

    return jsonify({
        "mensaje": "Vehiculo registrado correctamente",
        "datos": nueva_placa
    }), 201

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
