import requests
import json

class Configuraciones:
    def getEstado():
        return json.loads(requests.get("http://127.0.0.1:3000/consultarDatos").text)
    
    def getFechas():
        return json.loads(requests.get("http://127.0.0.1:3000/consultarFechas").text)
    
    def createMedicine(data):
        response = requests.post('http://127.0.0.1:5000/medicine', json= data)
        return json.loads(response.text)