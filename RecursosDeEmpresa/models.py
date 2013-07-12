#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TipoDocumento(models.Model):
    """Clase Tipo Documento 
    Atributos:Nombre,Descripción"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='Descripción')
    
    def __unicode__(self):
        return self.nombre 

class Barrio(models.Model):
    """Clase Barrio
    Atributo: nombre"""
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre
    
class Localidad(models.Model):
    """Clase Localidad
    Atributos: nombre, barrio"""
    nombre = models.CharField(max_length=100)
    barrio = models.ForeignKey(Barrio)
    
    def __unicode__(self):
        return self.nombre
    
class Domicilio(models.Model):
    """Clase Domicilio
    Atributos: direccion, numero, piso, depto, piso, codigo postal, barrio"""
    direccion = models.CharField(max_length=250, verbose_name='Dirección')
    numero = models.IntegerField(verbose_name='Número')
    piso = models.IntegerField()
    depto = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=100)
    barrio = models.ForeignKey(Barrio)
    
    def __unicode__(self):
        return self.direccion 
    
class Persona(models.Model):
    """Clase Persona
    Atributos: nombre, apellido, sexo, email, numero_documento, tipo_documento, domicilio, usuario"""
    sexo_choise= (
                  ('F','Femenino'),
                  ('M','Masculino'),
                  )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo =  models.CharField(max_length=1, choices=sexo_choise)
    email = models.EmailField(max_length=50)
    tipo_documento= models.ForeignKey(TipoDocumento)
    numero_documento = models.IntegerField(max_length=100)
    domicilio = models.ForeignKey(Domicilio)
    usuario = models.ForeignKey(User)
#    telefono_particular = models.ForeignKey(TelefonoPersona)
#    Telefono_domicilio = models.ForeignKey(TelefonoPersona)
    
    def __unicode__(self):
        return self.nombre + self.apellido
    
class TelefonoPersona(models.Model):
    """ Clase TelefonoPersona
    Atributos: numero, descripcion(Ej:casa,trabajo,privado)"""
    numero = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.numero
    
class TelefonoSucursal(models.Model):
    """Clase TelfonoSucursal
    Atributos: numero, sucursal"""
    numero = models.CharField(max_length=100)
#    sucursal = models.ForeignKey(Sucursal)
    
    def __unicode__(self):
        return self.numero
    
class Turno(models.Model):
    """Clase Turno
    Atributos: codigo, descripcion"""
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.codigo
    
class CalificacionServicio(models.Model):
    """Clase Calificacion Servicio
    Atributos:  nombre, descripcion"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='Descripción')
    
    def __unicode__(self):
        return self.nombre
    
class Sucursal(models.Model):
    """ Clase Sucursal
    Atributos: codigo, nombre, domicilio, calificacion_servicio, imagen"""
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100) 
    domicilio = models.ForeignKey(Domicilio)
    calificacion_servicio = models.ForeignKey(CalificacionServicio)
    imagen = models.ImageField(upload_to='/imagenes', verbose_name='Imágen')
    
    def __unicode__(self):
        return self.nombre
    
class Empleado(Persona, models.Model):
    """Clase Empleado hereda los atributos de Persona
    Atributos: legajo, turno, sucursal"""
    legajo = models.IntegerField(primary_key=True, unique=True)
    turno = models.ForeignKey(Turno)
    sucursal = models.ForeignKey(Sucursal)
    
    def __unicode__(self):
        return self.legajo
    
    