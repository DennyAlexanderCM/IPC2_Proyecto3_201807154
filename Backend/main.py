from flask import Flask, jsonify, request
from functions import *

app = Flask(__name__)
@app.route("/consultar", methods=['GET'])
def consultarDatos():
    return jsonify({"Estado":"Realizado"})

@app.route("/resivido", methods=['POST'])
def recibido():
    body = request.get_json()
    print(body["Saludo"])
    return jsonify({"Estado":"Realizado"})

# RECIBE LAS CONFIGURACIONES DEL SISTEMA
@app.route("/configuration", methods=['POST'])
def loadSettings():
    body = request.get_data()
    XMLSystemConfiguration(body)
    return jsonify({"Estado":"Realizado"})




#load data
@app.route("/load", methods=['POST'])
def loadData():
    #nombre = request.json['nombre']
    #OBTENEMOS LOS DATOS DEL REQUEST
    content = (request.get_data())
     # object = {"Mensaje":"Se hizo el POST correctamente"}





#INICIAR LA APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)