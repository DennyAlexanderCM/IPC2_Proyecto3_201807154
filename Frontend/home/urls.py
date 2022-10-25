from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('configuraciones/', views.loadSettings, name="configuraciones"),
    path('consumos/', views.loadSettingsMessages, name="consumos"),
    path('datos/', views.viewData, name="datos"),
    path('estudiante/', views.viewProfile, name="datosEstudiante"),
    path('selecionarfecha/', views.viewDates, name="selectDates"),
    path('crearelementos/', views.createData, name="crearElementos"),
    path('sources/', views.createResourse, name="crearRecurso"),
    path('categories/', views.createCategory, name="crearCategoria"),
    path('client/', views.createClient, name="crearCliente"),
    path('configuration/', views.createConfig, name="crearConfiguracion"),
    path('instance/', views.createInstance, name="crearInstancia"),
    path('cancelinstance/', views.cancelInstance, name="cancelarInstancia"),
]