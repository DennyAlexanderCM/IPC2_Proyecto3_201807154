class Cliente:
    def __init__(self, nit_cliente, nombre, usuario, clave, direccion, correo_electronico):
        self.nit_cliente = nit_cliente
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.lista_instancias = []
    
    def getNitCiente(self):
        return self.nit_cliente
    
    def getNombre(self):
        return self.nombre
    
    def getUsuario(self):
        return self.usuario
    
    def getClave(self):
        return self.clave
    
    def getDireccion(self):
        return self.direccion
    
    def getCorreoElectronico(self):
        return self.correo_electronico
    
    def getListaInstacncias(self):
        return self.lista_instancias
    
    def setNitCiente(self, nit_cliente):
        self.nit_cliente = nit_cliente
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getUsuario(self):
        return self.usuario
    
    def setClave(self, clave):
        self.clave = clave
    
    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def setCorreoElectronico(self, correo_electronico):
        self.correo_electronico = correo_electronico
    
    def añadirInstacncias(self, instancia):
        self.lista_instancias.append(instancia)

class Instancia:
    def __init__(self, id_instancia, id_configuracion, nombre, fecha_inicio, estado_instancia):
        self.id_instancia = id_instancia
        self.id_configuracion = id_configuracion
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.estado_instacia = estado_instancia
        self.fecha_final = None
        self.facturado = False
    
    def getIdInstancia(self):
        return self.id_instancia
    
    def getIdConfiguracion(self):
        return self.id_configuracion
    
    def getNombre(self):
        return self.nombre
    
    def getFechaInicio(self):
        return self.fecha_inicio
    
    def getEstado(self):
        return self.estado_instacia
    
    def getFechaFinal(self):
        return self.fecha_final
    
    def getFacturado(self):
        return self.facturado
    
    def setFechaFinal(self, fecha_final):
        self.fecha_final = fecha_final
    
    def Facturar(self):
        self.facturado = True
    
    
    