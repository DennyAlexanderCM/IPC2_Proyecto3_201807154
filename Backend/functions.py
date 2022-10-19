from xml.dom.minidom import *
import re
from Clases import *
from Clases.cliente import Instancia
from Clases.configuracion import Recurso_2
from Clases.consumo import Consumo

def XMLSystemConfiguration(xml):
    doc = parseString(xml)
    # Elemento raíz del documento
    rootNode = doc.documentElement
    lista_recursos = rootNode.getElementsByTagName("listaRecursos")[0]
    recursos = lista_recursos.getElementsByTagName("recurso")

    bd = parse('Datos/Configuraciones.xml')
    rootNodeConfiguraciones = bd.documentElement
    recursos_configuraciones = rootNodeConfiguraciones.getElementsByTagName('recursos')[0]
    categorias_configuraciones = rootNodeConfiguraciones.getElementsByTagName('categorias')[0]

    for recurso in recursos:
        
        id_recurso = recurso.getAttribute("id")
        nombre_recurso = recurso.getElementsByTagName("nombre")[0].firstChild.data
        abreviatura_recurso = recurso.getElementsByTagName("abreviatura")[0].firstChild.data
        metrica_recurso = recurso.getElementsByTagName("metrica")[0].firstChild.data
        tipo_recurso = recurso.getElementsByTagName("tipo")[0].firstChild.data
        Valor_hora_recurso = recurso.getElementsByTagName("valorXhora")[0].firstChild.data
        # ----------------------------------------------
        elemento_recurso = bd.createElement("recurso")
        elemento_recurso.setAttribute("id"  , id_recurso)
        elemento_recurso.setAttribute("nombre"  , nombre_recurso)
        abreviatura_config = bd.createElement("abreviatura")
        abreviatura_config.appendChild(bd.createTextNode(abreviatura_recurso))
        elemento_recurso.appendChild(abreviatura_config)
        metrica_config = bd.createElement("metrica")
        metrica_config.appendChild(bd.createTextNode(metrica_recurso))
        elemento_recurso.appendChild(metrica_config)
        tipo_config = bd.createElement("tipo")
        tipo_config.appendChild(bd.createTextNode(tipo_recurso))
        elemento_recurso.appendChild(tipo_config)
        valor_hora_config = bd.createElement("valorXhora")
        valor_hora_config.appendChild(bd.createTextNode(Valor_hora_recurso.strip()))
        elemento_recurso.appendChild(valor_hora_config)
        recursos_configuraciones.appendChild(elemento_recurso)

    categorias = rootNode.getElementsByTagName("categoria")
    
    for categoria in categorias:
        id_categoria = categoria.getAttribute("id")
        nombre_categoria = categoria.getElementsByTagName("nombre")[0].firstChild.data
        descripcion_categoria = categoria.getElementsByTagName("descripcion")[0].firstChild.data
        carga_trabajo_categoria = categoria.getElementsByTagName("cargaTrabajo")[0].firstChild.data
        # ----------------------------------------------
        elemento_categoria = bd.createElement("categoria")
        elemento_categoria.setAttribute("id"  , id_categoria)
        elemento_categoria.setAttribute("nombre"  , nombre_categoria)
        descripcion_config = bd.createElement("descripcion")
        descripcion_config.appendChild(bd.createTextNode(descripcion_categoria))
        elemento_categoria.appendChild(descripcion_config)
        carga_trabajo_config = bd.createElement("cargaTrabajo")
        carga_trabajo_config.appendChild(bd.createTextNode(carga_trabajo_categoria))
        elemento_categoria.appendChild(carga_trabajo_config)
        configuraciones = categoria.getElementsByTagName("configuracion")
        elemento_configuraciones = bd.createElement("configuraciones")
        for configuracion in configuraciones:
            id_configuracion = configuracion.getAttribute("id")
            nombre_configuracion = configuracion.getElementsByTagName("nombre")[0].firstChild.data
            descripcion_configuracion = configuracion.getElementsByTagName("descripcion")[0].firstChild.data
            # ----------------------------------------------
            elemento_configuracion = bd.createElement("configuracion")
            elemento_configuracion.setAttribute("id"  , id_configuracion)
            elemento_configuracion.setAttribute("nombre"  , nombre_configuracion)
            descripcion_cnfg = bd.createElement("descripcion")
            descripcion_cnfg.appendChild(bd.createTextNode(descripcion_configuracion))
            elemento_configuracion.appendChild(descripcion_cnfg)
    
            recursos_configuracion = configuracion.getElementsByTagName("recurso")
            elemento_recursos = bd.createElement("Recursos")
            for recurso in recursos_configuracion:
                id = recurso.getAttribute("id")
                cantidad_recurso = recurso.firstChild.data
                 # ----------------------------------------------
                elemento_recurso = bd.createElement("recurso")
                elemento_recurso.setAttribute("id", id)
                elemento_recurso.appendChild(bd.createTextNode(cantidad_recurso.strip()))
                elemento_recursos.appendChild(elemento_recurso)

            elemento_configuracion.appendChild(elemento_recursos)
            elemento_configuraciones.appendChild(elemento_configuracion)
        elemento_categoria.appendChild(elemento_configuraciones)
        categorias_configuraciones.appendChild(elemento_categoria)
    
    
    xml = Node.toxml(bd)
    f =  open("Datos/Configuraciones.xml", "w", encoding='utf-8')    
    f.write(xml)
    f.close()

def XMLSystemConfigurationClients(xml):
    doc = parseString(xml)
    datos = []
    numero_clientes = 0
    numero_instancias = 0
    # Elemento raíz del documento
    rootNode = doc.documentElement
    
    bd = parse('Datos/Clientes.xml')
    rootNodeConfiguraciones = bd.documentElement
    clientes_configuraciones = rootNodeConfiguraciones.getElementsByTagName('clientes')[0]
    clientes = rootNode.getElementsByTagName("cliente")
    for cliente in clientes:
        nit_cliente = cliente.getAttribute("nit")
        nombre_cliente = cliente.getElementsByTagName("nombre")[0].firstChild.data
        usuario_cliente = cliente.getElementsByTagName("usuario")[0].firstChild.data
        clave_cliente = cliente.getElementsByTagName("clave")[0].firstChild.data
        direcion_cliente = cliente.getElementsByTagName("direccion")[0].firstChild.data
        correo_electronico = cliente.getElementsByTagName("correoElectronico")[0].firstChild.data
         # ----------------------------------------------
        elemento_cliente = bd.createElement("cliente")
        elemento_cliente.setAttribute("nit", nit_cliente)
        elemento_cliente.setAttribute("nombre", nombre_cliente)
        usuario_config = bd.createElement("usuario")
        usuario_config.appendChild(bd.createTextNode(usuario_cliente))
        elemento_cliente.appendChild(usuario_config)
        clave_config = bd.createElement("clave")
        clave_config.appendChild(bd.createTextNode(clave_cliente))
        elemento_cliente.appendChild(clave_config)
        direccion_config = bd.createElement("direccion")
        direccion_config.appendChild(bd.createTextNode(direcion_cliente))
        elemento_cliente.appendChild(direccion_config)
        correo_config = bd.createElement("correoElectronico")
        correo_config.appendChild(bd.createTextNode(correo_electronico))
        elemento_cliente.appendChild(correo_config)
        elemento_instancias = bd.createElement("instancias")
        listas_instancias_cliente = cliente.getElementsByTagName("instancia")

        for instancia in listas_instancias_cliente:
            id_instancia = instancia.getAttribute("id")
            id_configuracion_instancia = instancia.getElementsByTagName("idConfiguracion")[0].firstChild.data
            nombre_instacia = instancia.getElementsByTagName("nombre")[0].firstChild.data
            fecha_inicio_instancia = instancia.getElementsByTagName("fechaInicio")[0].firstChild.data
            estado_instancia = instancia.getElementsByTagName("estado")[0].firstChild.data
            if estado_instancia.strip() == "Cancelada":
                fecha_fin_instancia = instancia.getElementsByTagName("fechaFinal")[0].firstChild.data
            # ----------------------------------------------
            elemento_instancia = bd.createElement("instancia")
            elemento_instancia.setAttribute("id", id_instancia)
            elemento_instancia.setAttribute("nombre", nombre_instacia)
            elemento_instancia.setAttribute("estado", "pendiente")
            id_config = bd.createElement("idConfiguracion")
            id_config.appendChild(bd.createTextNode(id_configuracion_instancia))
            elemento_instancia.appendChild(id_config)
            fecha_inicio = bd.createElement("fechaInicio")
            fecha_inicio.appendChild(bd.createTextNode(extractDate(fecha_inicio_instancia)))
            elemento_instancia.appendChild(fecha_inicio)
            estado_instancia_config = bd.createElement("estado")
            estado_instancia_config.appendChild(bd.createTextNode(estado_instancia))
            elemento_instancia.appendChild(estado_instancia_config)
            if estado_instancia.strip() == "Cancelada":
                fecha_fin = bd.createElement("fechaFinal")
                fecha_fin.appendChild(bd.createTextNode(extractDate(fecha_fin_instancia)))
                elemento_instancia.appendChild(fecha_fin)
            elemento_instancias.appendChild(elemento_instancia)
            numero_instancias += 1
        elemento_cliente.appendChild(elemento_instancias)
        clientes_configuraciones.appendChild(elemento_cliente)
        numero_clientes += 1
    
    # ESCRITURA EN LA BASE DE DATOS
    xml = Node.toxml(bd)
    f =  open("Datos/Clientes.xml", "w", encoding='utf-8')    
    f.write(xml)
    f.close()
    datos = {"Clientes":numero_clientes, "Instancias":numero_instancias}
    return datos

def XMLSystemConfigurationUse(xml):
    numero_consumos = 0

    doc = parseString(xml)
    # Elemento raíz del documento
    rootNode = doc.documentElement
    lista_comsumos = rootNode.getElementsByTagName("consumo")

    bd = parse('Datos/Consumos.xml')
    recursos_configuraciones = bd.documentElement


    for consumo in lista_comsumos:
        nit_cliente = consumo.getAttribute("nitCliente")
        id_configuracion = consumo.getAttribute("idInstancia")
        tiempo_consumido = consumo.getElementsByTagName("tiempo")[0].firstChild.data
        fecha_hora = consumo.getElementsByTagName("fechaHora")[0].firstChild.data
         # ----------------------------------------------
        elemento_consumo = bd.createElement("consumo")
        elemento_consumo.setAttribute("nitCliente", nit_cliente)
        elemento_consumo.setAttribute("idInstancia", id_configuracion)

        tiempo_consumido_config = bd.createElement("tiempo")
        tiempo_consumido_config.appendChild(bd.createTextNode(tiempo_consumido.strip()))
        elemento_consumo.appendChild(tiempo_consumido_config)
        fecha_hora_config = bd.createElement("fechaHora")
        fecha_hora_config.appendChild(bd.createTextNode(fecha_hora))
        elemento_consumo.appendChild(fecha_hora_config)
        recursos_configuraciones.appendChild(elemento_consumo)
        numero_consumos += 1

    xml = Node.toxml(bd)
    f =  open("Datos/Consumos.xml", "w", encoding='utf-8')    
    f.write(xml)
    f.close()
    respuesta = {"Consumos":numero_consumos}
    return respuesta

def extractDate(txt):
    searchDate = re.compile(r'([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})')
    obtenido = searchDate.search(txt)
    if obtenido:
        return obtenido[0]
    else:
        return "Ninguno"

def extractDateTime(txt):
    searchDate = re.compile(r'([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})(\s)([0-1][0-9]|2[0-3])(:)([0-5][0-9])')
    obtenido = searchDate.search(txt)
    if obtenido:
        return obtenido[0]
    else:
        return None

def refreshDataCategories():
    categorias_lista = []
    doc = parse('Datos/Configuraciones.xml')
    # Elemento raíz del documento
    rootNode = doc.documentElement
    categorias = rootNode.getElementsByTagName("categoria")
    
    for categoria in categorias:
        id_categoria = categoria.getAttribute("id")
        nombre_categoria = categoria.getAttribute("nombre")
        descripcion_categoria = categoria.getElementsByTagName("descripcion")[0].firstChild.data
        carga_trabajo_categoria = categoria.getElementsByTagName("cargaTrabajo")[0].firstChild.data
        categoria_objeto = Categoria(id_categoria, nombre_categoria, descripcion_categoria, carga_trabajo_categoria)
        
        configuraciones = categoria.getElementsByTagName("configuracion")
        for configuracion in configuraciones:
            id_configuracion = configuracion.getAttribute("id")
            nombre_configuracion = configuracion.getAttribute("nombre")
            descripcion_configuracion = configuracion.getElementsByTagName("descripcion")[0].firstChild.data
            configuracion_objeto = Configuracion(id_configuracion, nombre_configuracion, descripcion_configuracion)
            recursos_configuracion = configuracion.getElementsByTagName("recurso")
            
            for recurso in recursos_configuracion:
                id = recurso.getAttribute("id")
                cantidad_recurso = recurso.firstChild.data
                configuracion_objeto.añadirRecurso(Recurso_2(id, cantidad_recurso))
            categoria_objeto.añadirConfiguracion(configuracion_objeto)
        categorias_lista.append(categoria_objeto)
    
    return categorias_lista

def refreshDataResources():
    recursos_lista = []
    doc = parse('Datos/Configuraciones.xml')
    # Elemento raíz del documento
    rootNode = doc.documentElement
    lista_recursos = rootNode.getElementsByTagName("recursos")[0]
    recursos = lista_recursos.getElementsByTagName("recurso")

    for recurso in recursos:
        id_recurso = recurso.getAttribute("id")
        nombre_recurso = recurso.getAttribute("nombre")
        abreviatura_recurso = recurso.getElementsByTagName("abreviatura")[0].firstChild.data
        metrica_recurso = recurso.getElementsByTagName("metrica")[0].firstChild.data
        tipo_recurso = recurso.getElementsByTagName("tipo")[0].firstChild.data
        Valor_hora_recurso = recurso.getElementsByTagName("valorXhora")[0].firstChild.data
        recursos_lista.append(Recurso(id_recurso, nombre_recurso, abreviatura_recurso, metrica_recurso, tipo_recurso, Valor_hora_recurso))
    
    return recursos_lista

def refreshDataResourcesClient():
    cliente_lista = []
    doc = parse('Datos/Clientes.xml')
    # Elemento raíz del documento
    rootNode = doc.documentElement
    clientes = rootNode.getElementsByTagName("cliente")
    for cliente in clientes:
        nit_cliente = cliente.getAttribute("nit")
        nombre_cliente = cliente.getAttribute("nombre")
        usuario_cliente = cliente.getElementsByTagName("usuario")[0].firstChild.data
        clave_cliente = cliente.getElementsByTagName("clave")[0].firstChild.data
        direcion_cliente = cliente.getElementsByTagName("direccion")[0].firstChild.data
        correo_electronico = cliente.getElementsByTagName("correoElectronico")[0].firstChild.data
        cliente_objeto = Cliente(nit_cliente, nombre_cliente, usuario_cliente, clave_cliente,direcion_cliente, correo_electronico)
        
        listas_instancias_cliente = cliente.getElementsByTagName("instancia")

        for instancia in listas_instancias_cliente:
            id_instancia = instancia.getAttribute("id")
            nombre_instacia = instancia.getAttribute("nombre")
            id_configuracion_instancia = instancia.getElementsByTagName("idConfiguracion")[0].firstChild.data
            estado_instancia_facturado = instancia.getElementsByTagName("estado")[0].firstChild.data
            fecha_inicio_instancia = instancia.getElementsByTagName("fechaInicio")[0].firstChild.data
            estado_instancia = instancia.getElementsByTagName("estado")[0].firstChild.data
            instancia_objeto = Instancia(id_instancia, id_configuracion_instancia, nombre_instacia, fecha_inicio_instancia, estado_instancia)
            if estado_instancia.strip() == "Cancelada":
                fecha_fin_instancia = instancia.getElementsByTagName("fechaFinal")[0].firstChild.data
                instancia_objeto.setFechaFinal(fecha_fin_instancia)
            if not(estado_instancia_facturado == "pendiente"):
                instancia_objeto.Facturar()
                
            cliente_objeto.añadirInstacncias(instancia_objeto)
        cliente_lista.append(cliente_objeto)
    return cliente_lista

def refreshDataResourcesUse():
    consumos_lista = []
    doc = parse("Datos/Consumos.xml")
    # Elemento raíz del documento
    rootNode = doc.documentElement
    lista_comsumos = rootNode.getElementsByTagName("consumo")

    for consumo in lista_comsumos:
        nit_cliente = consumo.getAttribute("nitCliente")
        id_configuracion = consumo.getAttribute("idInstancia")
        tiempo_consumido = consumo.getElementsByTagName("tiempo")[0].firstChild.data
        print(tiempo_consumido )
        fecha_hora = consumo.getElementsByTagName("fechaHora")[0].firstChild.data
        consumos_lista.append(Consumo(nit_cliente, id_configuracion, tiempo_consumido, fecha_hora))

    return consumos_lista

def returnDataCategories():
    categorias_lista = []
    doc = parse('Datos/Configuraciones.xml')
    # Elemento raíz del documento
    rootNode = doc.documentElement
    categorias = rootNode.getElementsByTagName("categoria")
    
    for categoria in categorias:
        id_categoria = categoria.getAttribute("id")
        nombre_categoria = categoria.getAttribute("nombre")
        descripcion_categoria = categoria.getElementsByTagName("descripcion")[0].firstChild.data
        carga_trabajo_categoria = categoria.getElementsByTagName("cargaTrabajo")[0].firstChild.data
        configuraciones_lista = []
        configuraciones = categoria.getElementsByTagName("configuracion")
        for configuracion in configuraciones:
            id_configuracion = configuracion.getAttribute("id")
            nombre_configuracion = configuracion.getAttribute("nombre")
            descripcion_configuracion = configuracion.getElementsByTagName("descripcion")[0].firstChild.data
            recursos_lista = []
            recursos_configuracion = configuracion.getElementsByTagName("recurso")
            
            for recurso in recursos_configuracion:
                id = recurso.getAttribute("id")
                cantidad_recurso = recurso.firstChild.data
                recursos_lista.append({"id":id, "cantidadRecurso":cantidad_recurso})
            configuraciones_lista.append({"id":id_configuracion, "nombre":nombre_configuracion, "descripcion":descripcion_configuracion, "recursos":recursos_lista})
        categorias_lista.append({"id":id_categoria, "nombre":nombre_categoria, "descripcion":descripcion_categoria, "carga":carga_trabajo_categoria, "configuraiones":configuraciones_lista})
    
    return categorias_lista

def returnDataResourses():
    recursos_lista = []
    doc = parse('Datos/Configuraciones.xml')
    # Elemento raíz del documento
    rootNode = doc.documentElement
    lista_recursos = rootNode.getElementsByTagName("recursos")[0]
    recursos = lista_recursos.getElementsByTagName("recurso")

    for recurso in recursos:
        id_recurso = recurso.getAttribute("id")
        nombre_recurso = recurso.getAttribute("nombre")
        abreviatura_recurso = recurso.getElementsByTagName("abreviatura")[0].firstChild.data
        metrica_recurso = recurso.getElementsByTagName("metrica")[0].firstChild.data
        tipo_recurso = recurso.getElementsByTagName("tipo")[0].firstChild.data
        Valor_hora_recurso = recurso.getElementsByTagName("valorXhora")[0].firstChild.data
        recursos_lista.append({"id":id_recurso, "nombre":nombre_recurso, "abreviatura":abreviatura_recurso, "metrica":metrica_recurso, "tipo":tipo_recurso, "valorXhora":Valor_hora_recurso})
    return recursos_lista

def returnDataClients():
    cliente_lista = []
    doc = parse('Datos/Clientes.xml')
    # Elemento raíz del documento
    rootNode = doc.documentElement
    clientes = rootNode.getElementsByTagName("cliente")
    for cliente in clientes:
        nit_cliente = cliente.getAttribute("nit")
        nombre_cliente = cliente.getAttribute("nombre")
        usuario_cliente = cliente.getElementsByTagName("usuario")[0].firstChild.data
        clave_cliente = cliente.getElementsByTagName("clave")[0].firstChild.data
        direcion_cliente = cliente.getElementsByTagName("direccion")[0].firstChild.data
        correo_electronico = cliente.getElementsByTagName("correoElectronico")[0].firstChild.data
        lista_intancias = []

        listas_instancias_cliente = cliente.getElementsByTagName("instancia")

        for instancia in listas_instancias_cliente:
            id_instancia = instancia.getAttribute("id")
            nombre_instacia = instancia.getAttribute("nombre")
            id_configuracion_instancia = instancia.getElementsByTagName("idConfiguracion")[0].firstChild.data
            estado_instancia_facturado = instancia.getElementsByTagName("estado")[0].firstChild.data
            fecha_inicio_instancia = instancia.getElementsByTagName("fechaInicio")[0].firstChild.data
            estado_instancia = instancia.getElementsByTagName("estado")[0].firstChild.data
            if estado_instancia.strip() == "Cancelada":
                fecha_fin_instancia = instancia.getElementsByTagName("fechaFinal")[0].firstChild.data
                lista_intancias.append({"id":id_instancia, "nombre":nombre_instacia, "Configuracion":id_configuracion_instancia, "fechaInicio": fecha_inicio_instancia, "estado":estado_instancia, "fechaFin":fecha_fin_instancia})
            else:
                lista_intancias.append({"id":id_instancia, "nombre":nombre_instacia, "Configuracion":id_configuracion_instancia, "fechaInicio": fecha_inicio_instancia, "estado":estado_instancia})
        cliente_lista.append({"nit":nit_cliente, "nombre":nombre_cliente, "usuario":usuario_cliente, "clave":clave_cliente, "direccion": direcion_cliente, "correo":correo_electronico, "instancias":lista_intancias}) 
    return cliente_lista

def resetData():
    clientes = '<?xml version="1.0" ?><base_de_datos><clientes></clientes></base_de_datos>'
    configuraciones = '<?xml version="1.0"?><base_de_datos><recursos></recursos><categorias></categorias></base_de_datos>'
    consumos = '<?xml version="1.0"?><base_de_datos></base_de_datos>'

    f =  open("Datos/Consumos.xml", "w", encoding='utf-8')    
    f.write(consumos)
    f.close()
    f =  open("Datos/Clientes.xml", "w", encoding='utf-8')    
    f.write(clientes)
    f.close()
    f =  open("Datos/Configuraciones.xml", "w", encoding='utf-8')    
    f.write(configuraciones)
    f.close()

