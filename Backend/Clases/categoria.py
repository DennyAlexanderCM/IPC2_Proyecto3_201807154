class Categoria:
    def __init__(self, id_categoria, nombre, descripcion, carga_trabajo):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.carga_trabajo = carga_trabajo
        self.lista_configuraciones = []
    
    # GET AND SET
    def getIdCategoria(self):
        return self.id_categoria
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getCargaTrabajo(self):
        return self.carga_trabajo
    
    def getListaConfiguraciones(self):
        return self.lista_configuraciones
    
    def setIdCategoria(self, id_categoria):
        self.id_categoria = id_categoria
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def setCargaTrabajo(self,carga_trabajo ):
        self.carga_trabajo = carga_trabajo
    
    def añadirConfiguracion(self, configuracion):
        self.lista_configuraciones.append(configuracion)