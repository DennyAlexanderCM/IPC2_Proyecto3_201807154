class Configuracion:
    def __init__(self, id_configuracion, nombre, descripcion):
        self.id_configuracion = id_configuracion
        self.nombre = nombre
        self.descripcion = descripcion
        self.lista_recursos = []

        # GET AND SET
    def getIdConfiguracion(self):
        return self.id_categoria
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getListaRecursos(self):
        return self.lista_recursos
    
    def setIdConfiguracion(self, id_configuracion):
        self.id_configuracion = id_configuracion
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def añadirRecurso(self, recurso):
        self.lista_recursos.append(recurso)

class Recurso_2:
    def __init__(self, id_recurso, cantidad_recurso):
        self.id_recurso = id_recurso
        self.cantidad_recurso = cantidad_recurso
    
    def getIdRecurso(self):
        return self.id_recurso
    
    def getCantidadRecurso(self):
        return self.cantidad_recurso
    
    def setIdRecurso(self, id_recurso):
        self.id_recurso = id_recurso
    
    def setCantidadRecurso(self, cantidad_recurso):
        self.cantidad_recurso = cantidad_recurso
    