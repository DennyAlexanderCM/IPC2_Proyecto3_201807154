class Recurso:
    def __init__(self, id_recurso, nombre, abreviatura, metrica, tipo, valor_hora):
        self.id_recurso = id_recurso
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.metrica = metrica
        self.tipo = tipo
        self.valor_hora = valor_hora
    
    # GET AND SET
    def getIdCurso(self):
        return self.id_recurso
    
    def getNombre(self):
        return self.nombre
    
    def getAbreviatura(self):
        return self.abreviatura
    
    def getMetrica(self):
        return self.metrica
    
    def getTipo(self):
        return self.tipo
    
    def getValorHora(self):
        return self.valor_hora
    
    def setIdCurso(self, id_recurso):
        self.id_recurso = id_recurso
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setAbreviatura(self, breviatura):
        self.abreviatura = breviatura
    
    def setMetrica(self, metrica):
        self.metrica = metrica
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getValorHora(self, alor_hora):
        self.valor_hora = alor_hora