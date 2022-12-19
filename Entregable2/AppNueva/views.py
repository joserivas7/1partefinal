from django.shortcuts import render 
from django.template import loader
from django.http import HttpResponse
from AppNueva.models import Empleado , Estudiante , Persona
from AppNueva.forms import PersonaForm, EstudianteForm, EmpleadoForm 



# Create your views here.


def personas (request):
    return render(request, "AppNueva/Personas.html")

def crearpersona (request):
    if request.method=="POST":
        form= PersonaForm(request.POST)

        if form.is_valid():
            informacion= form.cleaned_data #convierte el formulario en un diccionario para poder manejarlo y guardarlo en la DB.
            print(informacion)
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            sexo= informacion["sexo"]
            dni= informacion["dni"]
            perso= Persona(nombre=nombre, apellido=apellido, sexo=sexo, dni=dni)
            perso.save()
            return render(request, "AppNueva/Inicio.html", {"mensaje": "Persona guardada"})
        else:
            return render(request, "AppNueva/crearpersona.html", {"mensaje2": "Informacion no Valida para guardar."})
    else:
        formulario= PersonaForm()
        return render(request, "AppNueva/crearpersona.html", {"form": formulario})


def busquedadni (request):
    return render(request, "AppNueva/busquedadni.html")


def buscar (request):
    dni= request.GET["dni"]
    if dni!="":
        perso= Persona.objects.filter(dni__icontains=dni)
        return render(request, "AppNueva/resultadobusqueda.html" ,{"perso":perso})
    else:
        return render(request, "AppNueva/busquedadni.html", {"mensaje":"Ingresa por favor un DNI"})






def estudiantes (request):
    return render(request, "AppNueva/Estudiantes.html")   

def crearestudiante (request):
    if request.method=="POST":
        form= EstudianteForm(request.POST)

        if form.is_valid():
            informacion= form.cleaned_data#convierte el formulario en un diccionario para poder manejarlo y guardarlo en la DB.
            print(informacion)
            nombre_estudiante= informacion["nombre_estudiante"]
            nombre_universidad= informacion["nombre_universidad"]
            carrera= informacion["carrera"]
            año_ingreso= informacion["año_ingreso"]
            estu= Estudiante(nombre_estudiante=nombre_estudiante, nombre_universidad=nombre_universidad, carrera=carrera, año_ingreso=año_ingreso)
            estu.save()
            return render(request, "AppNueva/Inicio.html", {"mensaje": "Estudiante guardado"})
        else:
            return render(request, "AppNueva/crearestudiante.html", {"mensaje": "Informacion no Valida para guardar."})
    else:
        formulario= EstudianteForm()
        return render(request, "AppNueva/crearestudiante.html", {"form": formulario})


def busquedacarrera (request):
    return render(request, "AppNueva/busquedacarrera.html")

def buscar2 (request):
    carrera= request.GET["carrera"]
    if carrera!="":
        estu= Estudiante.objects.filter(carrera__icontains=carrera)
        return render(request, "AppNueva/resultadobusqueda2.html" ,{"estu":estu})
    else:
        return render(request, "AppNueva/busquedacarrera.html", {"mensaje":"Ingresa por favor una carrera"})




def empleados (request):
    return render(request, "AppNueva/Empleados.html")

def crearempleado (request):
    if request.method=="POST":
        form= EmpleadoForm(request.POST)

        if form.is_valid():
            informacion= form.cleaned_data
            print(informacion)
            nombre_empleado= informacion["nombre_empleado"]
            nombre_empresa= informacion["nombre_empresa"]
            año_antiguedad= informacion["año_antiguedad"]
            sueldo= informacion["sueldo"]
            email= informacion["email"]
            emple= Empleado(nombre_empleado=nombre_empleado, nombre_empresa=nombre_empresa, año_antiguedad=año_antiguedad, sueldo=sueldo, email=email)
            emple.save()
            return render(request, "AppNueva/Inicio.html", {"mensaje": "Empleado guardado"})
        else:
            return render(request, "AppNueva/crearempleado.html", {"mensaje": "Informacion no Valida para guardar."})
    else:
        formulario= EmpleadoForm()
        return render(request, "AppNueva/crearempleado.html", {"form": formulario})


def busquedanombre (request):
    return render(request, "AppNueva/busquedanombre.html")

def buscar3 (request):
    nombre_empleado= request.GET["nombre_empleado"]
    if nombre_empleado!="":
        emple= Empleado.objects.filter(nombre_empleado__icontains=nombre_empleado)
        return render(request, "AppNueva/resultadobusqueda3.html" ,{"emple":emple})
    else:
        return render(request, "AppNueva/busquedanombre.html", {"mensaje":"Ingresa por favor un Nombre"})




def inicio(request):
    return render(request, "AppNueva/Inicio.html")
