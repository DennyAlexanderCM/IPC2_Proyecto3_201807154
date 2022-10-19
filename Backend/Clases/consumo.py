class Consumo:
    def __init__(self, nit_cliente, id_instancia, tiempo, fecha_hora):
        self.nit_cliente = nit_cliente
        self.id_instancia = id_instancia
        self.tiempo = tiempo
        self.fecha_hora = fecha_hora
    
    def getNitCliente(self):
        return self.nit_cliente
    
    def getIdInstancia(self):
        return self.id_instancia
    
    def getTiempo(self):
        return self.tiempo
    
    def getFechaHora(self):
        return self.fecha_hora