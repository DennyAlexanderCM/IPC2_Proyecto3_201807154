import requests
import json

class Configuraciones:
    def getEstado():
        return json.loads(requests.get("http://127.0.0.1:3000/consultar").text)