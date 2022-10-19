from flask import Flask, jsonify, request
from functions import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

configuraciones = []

# RECIBE LAS CONFIGURACIONES DEL SISTEMA
@app.route("/configuracion", methods=['POST'])
def configuraciones():
    body = request.get_data()
    XMLSystemConfiguration(body)
    resultados = XMLSystemConfigurationClients(body)
    return jsonify(resultados)

# RECIBE LAS CONFIGURACIONES DEL SISTEMA DE LOS CONSUMOS REALIZADOS
@app.route("/consumos", methods=['POST'])
def consumos():
    body = request.get_data()
    respuesta = XMLSystemConfigurationUse(body)
    return jsonify(respuesta)

# RECIBE LAS CONFIGURACIONES DEL SISTEMA
@app.route("/consultar", methods=['POST'])
def consultas():
    body = {}
    body["recursos"] = returnDataResourses()
    body["categorias"] = returnDataCategories()
    body["clientes"] = returnDataClients()
    return jsonify(body)

# ELIMINA LOS DATOS ALMACENADOS
@app.route("/reestablecer", methods=['POST'])
def restablecer():
    resetData()
    return jsonify({"mensaje":"Datos eliminados"})


#INICIAR LA APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)