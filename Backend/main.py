from flask import Flask, jsonify, request
from functions import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# RECIBE LAS CONFIGURACIONES DEL SISTEMA
@app.route("/configuration", methods=['POST'])
def configuraciones():
    body = request.get_data()
    XMLSystemConfiguration(body)
    resultados = XMLSystemConfigurationCustomers(body)
    return jsonify(resultados)

# RECIBE LAS CONFIGURACIONES DEL SISTEMA
@app.route("/consumos", methods=['POST'])
def consumos():
    body = request.get_data()
    respuesta = XMLSystemConfigurationUse(body)
    return jsonify(respuesta)


#INICIAR LA APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)