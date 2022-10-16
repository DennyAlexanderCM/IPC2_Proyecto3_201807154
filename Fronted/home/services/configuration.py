import requests
import json

class Configuraciones:
    def getEstado():
        print("hello")
        print(requests.get("http://127.0.0.1:3000/consultar").text)
        return json.loads(requests.get("http://127.0.0.1:3000/consultar").text)