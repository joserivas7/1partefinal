from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name="inicio"),
    
    path('personas/',personas, name="personas"),
    path('crearpersona/', crearpersona, name="crearpersona"),
    path('busquedadni/', busquedadni , name="busquedadni"),
    path('buscar/', buscar , name="buscar"),


    path('estudiantes/',estudiantes, name="estudiantes"),
    path('crearestudiante/', crearestudiante, name="crearestudiante"),
    path('busquedacarrera/', busquedacarrera , name="busquedacarrera"),
    path('buscar2/', buscar2 , name="buscar2"),
    
    path('empleados/',empleados, name="empleados"),
    path('crearempleado/', crearempleado, name="crearempleado"),
    path('busquedanombre/', busquedanombre , name="busquedanombre"),
    path('buscar3/', buscar3 , name="buscar3"),

]
