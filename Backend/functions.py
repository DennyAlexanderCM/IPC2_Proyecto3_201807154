from xml.dom import minidom
from xml.dom.expatbuilder import parseString
from recurso import Recurso
from categoria import Categoria
from configuracion import Configuracion, Recurso
from cliente import Cliente, Instancia
from linkend_list import LinkedList

def XMLSystemConfiguration(xml):
    #LISTA QUE CONTRENDRÁ CADA PACIENTE
    doc = parseString(xml)
    # Elemento raíz del documento
    rootNode = doc.documentElement
    lista_recursos = rootNode.getElementsByTagName("listaRecursos")[0]
    recursos = lista_recursos.getElementsByTagName("recurso")

    for recurso in recursos:
        id_recurso = recurso.getAttribute("id")
        nombre_recurso = recurso.getElementsByTagName("nombre")[0].firstChild.data
        abreviatura_recurso = recurso.getElementsByTagName("abreviatura")[0].firstChild.data
        metrica_recurso = recurso.getElementsByTagName("metrica")[0].firstChild.data
        tipo_recurso = recurso.getElementsByTagName("tipo")[0].firstChild.data
        Valor_hora_recurso = recurso.getElementsByTagName("valorXhora")[0].firstChild.data
        recursos_lista.append(Recurso(id_recurso, nombre_recurso, abreviatura_recurso, metrica_recurso, tipo_recurso, Valor_hora_recurso))

    categorias = rootNode.getElementsByTagName("categoria")
    
    for categoria in categorias:
        id_categoria = categoria.getAttribute("id")
        nombre_categoria = categoria.getElementsByTagName("nombre")[0].firstChild.data
        descripcion_categoria = categoria.getElementsByTagName("descripcion")[0].firstChild.data
        carga_trabajo_categoria = categoria.getElementsByTagName("cargaTrabajo")[0].firstChild.data
        objeto_categoria = Categoria(id_categoria, nombre_categoria, descripcion_categoria, carga_trabajo_categoria)
        
        configuraciones = categoria.getElementsByTagName("configuracion")
    
        for configuracion in configuraciones:
            id_configuracion = configuracion.getAttribute("id")
            nombre_configuracion = configuracion.getElementsByTagName("nombre")[0].firstChild.data
            descripcion_configuracion = configuracion.getElementsByTagName("descripcion")[0].firstChild.data
            objeto_configuracion = Configuracion(id_configuracion, nombre_configuracion, descripcion_configuracion)

            recursos_configuracion = configuracion.getElementsByTagName("recurso")
            
            for recurso in recursos_configuracion:
                id = recurso.getAttribute("id")
                cantidad_recurso = recurso.firstChild.data
                objeto_configuracion.añadirRecurso(Recurso(id, cantidad_recurso))
            
            objeto_categoria.añadirConfiguracion(objeto_configuracion)
        
        categorias_lista.append(objeto_categoria)
    
    clientes = rootNode.getElementsByTagName("cliente")
    for cliente in clientes:
        nit_cliente = cliente.getAttribute("nit")
        nombre_cliente = cliente.getElementsByTagName("nombre")[0].firstChild.data
        usuario_cliente = cliente.getElementsByTagName("usuario")[0].firstChild.data
        clave_cliente = cliente.getElementsByTagName("clave")[0].firstChild.data
        direcion_cliente = cliente.getElementsByTagName("direccion")[0].firstChild.data
        correo_electronico = cliente.getElementsByTagName("correoElectronico")[0].firstChild.data
        objeto_cliente = Cliente(nit_cliente, nombre_cliente, usuario_cliente, clave_cliente, direcion_cliente, correo_electronico)
        
        listas_instancias_cliente = cliente.getElementsByTagName("instancia")

        for instancia in listas_instancias_cliente:
            id_instancia = instancia.getAttribute("id")
            id_configuracion_instancia = instancia.getElementsByTagName("idConfiguracion")[0].firstChild.data
            nombre_instacia = instancia.getElementsByTagName("nombre")[0].firstChild.data
            fecha_inicio_instancia = instancia.getElementsByTagName("fechaInicio")[0].firstChild.data
            estado_instancia = instancia.getElementsByTagName("estado")[0].firstChild.data
            fecha_inicio_final = instancia.getElementsByTagName("fechaFinal")[0].firstChild.data
            objeto_cliente.añadirInstacncias(Instancia(id_instancia, id_configuracion_instancia, nombre_instacia, fecha_inicio_instancia, estado_instancia))
    print("¡Datos cargados!")

XMLSystemConfiguration()