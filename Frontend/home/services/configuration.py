import requests
import json

class Configuraciones:
    def getEstado():
        return json.loads(requests.get("http://127.0.0.1:3000/consultarDatos").text)
    
    def getFechas():
        return json.loads(requests.get("http://127.0.0.1:3000/consultarFechas").text)
    
    def createNewSourse(data):
        response = requests.post('http://127.0.0.1:3000/crearRecurso', json= data)
        return json.loads(response.text)

    def createNewCategories(data):
        response = requests.post('http://127.0.0.1:3000/crearCategoria', json= data)
        return json.loads(response.text)
    
    def createNewClient(data):
        response = requests.post('http://127.0.0.1:3000/crearCliente', json= data)
        return json.loads(response.text)
    
    def createNewConfiguration(data):
        response = requests.post('http://127.0.0.1:3000/crearConfiguracion', json= data)
        return json.loads(response.text)

    def createNewInstance(data):
        response = requests.post('http://127.0.0.1:3000/crearInstancia', json= data)
        return json.loads(response.text)
    
    def cancelInstance(data):
        response = requests.post('http://127.0.0.1:3000/cancelarInstancia', json= data)
        return json.loads(response.text)