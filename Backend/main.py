from flask import Flask, jsonify, request
from functions import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    body["Recursos"] = returnDataResources()
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

# CREAR RECURSO
@app.route("/crearRecurso", methods=['POST'])
def crarRecurso():
    body = request.get_json()
    addNewResourse(body["id"], body["nombre"], body["abreviatura"], body["metrica"], body["tipo"], body["valorXhora"])
    
    return jsonify({"Mensaje":"Correcto"})

# CREAR CATEGORÍA
@app.route("/crearCategoria", methods=['POST'])
def crarCategoria():
    body = request.get_json()
    addNewCategory(body["id"], body["nombre"], body["descripcion"], body["carga"])
    return jsonify({"Mensaje":"Correcto"})

# CREAR CONFIGURACIÓN
@app.route("/crearConfiguracion", methods=['POST'])
def crarConfiguracion():
    body = request.get_json()
    print(body["id_categoria"])
    addNewConfiguration(body["id_categoria"], body["id_config"], body["nombre"], body["descripcion"])
    
    return jsonify({"Mensaje":"Correcto"})

# CREAR CLIENTE
@app.route("/crearCliente", methods=['POST'])
def crarCliente():
    body = request.get_json()
    
    addNewClient(body["nit"], body["nombre"], body["usuario"], body["clave"], body["direccion"], body["correo"])
    return jsonify({"Mensaje":"Correcto"})

# CREAR iNSTANCIA
@app.route("/crearInstancia", methods=['POST'])
def crarInstancia():
    body = request.get_json()
    if body["estado"] == "Cancelada":
        print(body["fechaInicio"])
        addNewInstanceClient(body["nit"], body["id"], body["nombre"], body["idConfig"], body["fechaInicio"], body["estado"], body["fechaFin"])
    else:
        addNewInstanceClient(body["nit"], body["id"], body["nombre"], body["idConfig"], body["fechaInicio"], body["estado"])

    return jsonify({"Mensaje":"Correcto"})

# AÑADIR UN RECURSO A UNA CONFIGURACIÓN
@app.route("/crearRecursoConfiguracion", methods=['POST'])
def crarRecursoConfiguracion():
    body = request.get_json()
    addNewResourseConfiguration(body["id_config"], body["id_recurso"], body["cantidad"])
    
    return jsonify({"Mensaje":"Correcto"})

# CANCELA LA INSTANCIA DE UN CLIENTE
@app.route("/cancelarInstancia", methods=['POST'])
def cancelarInstancia():
    body = request.get_json()
    cancelarInstancias(body["nitCliente"], body["idInstancia"])
    return jsonify({"Mensaje":"Correcto"})

#INICIAR LA APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)