from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('configuraciones/', views.loadSettings, name="configuraciones"),
    path('consumos/', views.loadSettingsMessages, name="consumos"),
    path('datos/', views.viewData, name="datos"),
    
]