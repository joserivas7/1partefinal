from django.db import models 


# Create your models here.


class Persona (models.Model):
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    sexo= models.CharField (max_length=50)
    dni= models.IntegerField ()

    def __str__(self):
        return f"{(self.nombre)} - {(self.apellido)} - {(self.sexo)} - {str(self.dni)}"

class Estudiante (models.Model):
    nombre_estudiante = models.CharField (max_length=50)
    nombre_universidad = models.CharField (max_length=50)
    carrera = models.CharField (max_length=50)
    año_ingreso = models.DateField(auto_created=False , auto_now= False , blank=True)

    def __str__(self):
        return f"{(self.nombre_estudiante)} - {(self.nombre_universidad)} - {str(self.carrera)} - {str(self.año_ingreso)}"


class Empleado (models.Model):
    nombre_empleado = models.CharField (max_length=50)
    nombre_empresa = models.CharField (max_length=50)
    año_antiguedad = models.DateField (auto_created=False , auto_now= False , blank=True)
    sueldo = models.IntegerField ()
    email = models.EmailField (max_length=50)

    def __str__(self):
        return f"{(self.nombre_empleado)} - {(self.nombre_empresa)} - {str(self.año_antiguedad)} - {str(self.sueldo)} - {(self.email)}"


