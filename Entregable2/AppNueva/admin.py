from django.contrib import admin
from .models import Persona, Estudiante, Empleado

# Register your models here.


admin.site.register(Persona)
admin.site.register(Estudiante)
admin.site.register(Empleado)