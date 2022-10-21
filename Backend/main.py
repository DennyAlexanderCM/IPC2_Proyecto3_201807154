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

@app.route("/consultarDatos", methods=['GET'])
def consultas():
    body = {}
    body["Recursos"] = returnDataResourses()
    body["Categorias"] = returnDataCategories()
    body["Clientes"] = returnDataClients()
    return jsonify(body)

@app.route("/consultarFechas", methods=['GET'])
def consultasFechas():
    body = {}
    body["Fechas"] = returnDates()
    return jsonify(body)

# ELIMINA LOS DATOS ALMACENADOS
@app.route("/restablecer", methods=['GET'])
def restablecer():
    resetData()
    return jsonify({"Mensaje":"Datos eliminados correctamente"})

@app.route("/crearRecurso", methods=['POST'])
def crarRecurso():
    body = request.get_json()
    print(body["id"], body["nombre"], body["abreviatura"], body["metrica"], body["tipo"], body["valorXhora"])
    addNewResourse(body["id"], body["nombre"], body["abreviatura"], body["metrica"], body["tipo"], body["valorXhora"])
    
    return jsonify({"Mensaje":"Correcto"})



#INICIAR LA APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)