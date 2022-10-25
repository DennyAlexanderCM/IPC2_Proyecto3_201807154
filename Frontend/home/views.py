from cgitb import reset
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .services import Configuraciones
"""
def hello(request):
    return HttpResponse("Hello word")"""
def index(request):
    return render(request,"index.html")

def loadSettings(request):
    return render(request, "configuracion.html")

def loadSettingsMessages(request):
    return render(request, "consumidos.html")

def viewData(request):
    resultado = Configuraciones.getEstado()
    return render(request, "views.html", resultado)

def viewDates(request):
    resultado = Configuraciones.getFechas()
    return render(request, "seleccionarRango.html", resultado)

def viewDates(request):
    resultado = Configuraciones.getFechas()
    return render(request, "seleccionarRango.html", resultado)

def viewProfile(request):
    return render(request, "estudiante.html")

def createData(request):
    resultado = Configuraciones.getEstado()
    return render(request, "crearNuevos.html", resultado)


def createCategory(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("name")
        descripcion = request.POST.get("description")
        trabajo = request.POST.get("work")
        informacion = {"id":id, "nombre": nombre, "descripcion":descripcion, "carga":trabajo}
        respuesta = Configuraciones.createNewCategories(informacion)
        print(respuesta)
    return redirect("/crearelementos")

def createResourse(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("name")
        abreviatura = request.POST.get("abbreviation")
        metrica = request.POST.get("metrics")
        tipo = request.POST.get("type")
        valor = request.POST.get("value")
        informacion = {"id":id, "nombre": nombre, "abreviatura":abreviatura, "metrica":metrica, "tipo":tipo, "valorXhora":valor}
        respuesta = Configuraciones.createNewSourse(informacion)
        print(respuesta)
    return render(request, "crearNuevos.html")

def createClient(request):
    if request.method == "POST":
        id = request.POST.get("nit")
        nombre = request.POST.get("name")
        usuario = request.POST.get("user")
        clave = request.POST.get("code")
        direccion = request.POST.get("address")
        correo = request.POST.get("mail")
        informacion = {"nit":id, "nombre": nombre, "usuario":usuario, "clave":clave, "direccion":direccion, "correo":correo}
        respuesta = Configuraciones.createNewClient(informacion)
        print(informacion)
    return render(request, "crearNuevos.html")

def createConfig(request):
    if request.method == "POST":
        id_categoria = request.POST.get("categoria")
        id_config = request.POST.get("id")
        nombre = request.POST.get("name")
        descripcion = request.POST.get("description")
        informacion = {"id_categoria":id_categoria, "id_config": id_config, "nombre":nombre, "descripcion":descripcion}
        respuesta = Configuraciones.createNewConfiguration(informacion)
        print(informacion)
    return render(request, "crearNuevos.html")

def createInstance(request):
    if request.method == "POST":
        nit_cliente = request.POST.get("cliente")
        id_instancia = request.POST.get("id_instance")
        nombre = request.POST.get("name")
        fecha_inicio = request.POST.get("dateInit")
        estado = request.POST.get("estado")
        configuracion = request.POST.get("configuration")
        if estado == "2":
            fecha_Fin = request.POST.get("dateEnd")
            informacion = {"nit":nit_cliente, "id": id_instancia, "nombre":nombre, "fechaInicio":fecha_inicio, "estado":"Cancelada", "fechaFin":fecha_Fin, "idConfig":configuracion}
            respuesta = Configuraciones.createNewInstance(informacion)
        else:
            informacion = {"nit":nit_cliente, "id": id_instancia, "nombre":nombre, "fechaInicio":fecha_inicio, "estado":"Vigente", "idConfig":configuracion}
            respuesta = Configuraciones.createNewInstance(informacion)
            print(informacion)
    return render(request, "crearNuevos.html")

def cancelInstance(request):
    if request.method == "POST":
        seleccion = request.POST.get("instancia")
        if seleccion:
            seleccion = seleccion.split(";")
            nit_cliente = seleccion[0]
            id_instancia = seleccion[1]
            informacion = {"nitCliente":nit_cliente, "idInstancia":id_instancia}
            respuesta = Configuraciones.cancelInstance(informacion)
            print(informacion)
    return render(request, "crearNuevos.html")