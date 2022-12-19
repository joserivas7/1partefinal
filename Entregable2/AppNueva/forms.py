from django import forms


class PersonaForm (forms.Form):
    nombre = forms.CharField (label="nombre", max_length=50)
    apellido = forms.CharField (label="apellido", max_length=50)
    sexo= forms.CharField (label="sexo", max_length=50)
    dni= forms.IntegerField(label="dni")


class EstudianteForm (forms.Form):
    nombre_estudiante = forms.CharField (label="nombre_estudiante", max_length=50)
    nombre_universidad = forms.CharField (label="nombre_universidad", max_length=50)
    carrera = forms.CharField (label="carrera", max_length=50)
    año_ingreso = forms.DateField(label="año_ingreso")


class EmpleadoForm (forms.Form):
    nombre_empleado = forms.CharField (label="nombre_empleado", max_length=50)
    nombre_empresa = forms.CharField (label="nombre_empresa", max_length=50)
    año_antiguedad = forms.DateField (label="año_antiguedad")
    sueldo = forms.IntegerField (label="sueldo")
    email = forms.EmailField (label="email", max_length=50)
