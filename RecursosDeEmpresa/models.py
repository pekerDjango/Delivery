#encoding:utf-8
from django.db import models
# Create your models here.

class TipoDocumento(models.Model):
    """Clase Tipo Documento 
    Atributos:Nombre,Descripción"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='Descripción')
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipos de Documentos" 

class Barrio(models.Model):
    """Clase Barrio
    Atributo: nombre"""
    nombre = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.nombre
    
    
class Localidad(models.Model):
    """Clase Localidad
    Atributos: nombre, barrio"""
    nombre = models.CharField(max_length=100, unique=True)
    barrio = models.ManyToManyField(Barrio)    
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Localidades"
    
class Provincia(models.Model):
    """Clase Provincia
    Atributos: nombre, localidad"""
    nombre = models.CharField(max_length=100, unique=True)
    localidad = models.ManyToManyField(Localidad)
      
    def __unicode__(self):
        return self.nombre      
     
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
    email = models.EmailField(max_length=50, help_text='to@example.com')
    tipo_documento= models.ForeignKey(TipoDocumento)
    numero_documento = models.IntegerField(max_length=100)
    direccion = models.CharField(max_length=250, verbose_name='Dirección')
    numero_direccion = models.IntegerField(verbose_name='Número')
    piso = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=50, blank=True, null=True)
    codigo_postal = models.CharField(max_length=100, verbose_name="Código Postal")
    provincia = models.ForeignKey(Provincia)
    localidad = models.ForeignKey(Localidad)
    barrio = models.ForeignKey(Barrio)
#    usuario = models.OneToOneField(User)
    telefono_particular = models.CharField(max_length=100, help_text='Código de área + Nº. Ej.: 351-473-9643.', verbose_name="Teléfono Particular")
    telefono_domicilio =models.CharField(max_length=100, blank=True, null=True, help_text='Código de área + Nº. Ej.: 351-473-9643.', verbose_name="Teléfono Domicilio")
    
    def __unicode__(self):
        return self.nombre + self.apellido   
                 
class Turno(models.Model):
    """Clase Turno
    Atributos: codigo, descripcion"""
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    descripcion = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.descripcion
    
class CalificacionServicio(models.Model):
    """Clase Calificacion Servicio
    Atributos:  nombre, descripcion"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='Descripción')
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Calificación de Servicios"
    
class Sucursal(models.Model):
    """ Clase Sucursal
    Atributos: codigo, nombre, domicilio, calificacion_servicio, imagen"""
    
    def Vista_Previa(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)
    
    Vista_Previa.allow_tags = True
    
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField(max_length=100) 
    direccion = models.CharField(max_length=250, verbose_name='Dirección')
    numero_direccion = models.IntegerField(verbose_name='Número')
#    piso = models.IntegerField(blank=True)
#    depto = models.CharField(max_length=50,blank=True)
    codigo_postal = models.CharField(max_length=100, verbose_name="Código Postal")
    barrio = models.ForeignKey(Barrio)
    localidad = models.ForeignKey(Localidad)
    calificacion_servicio = models.ForeignKey(CalificacionServicio)
    imagen = models.ImageField(upload_to='imagenes/Sucursales', verbose_name='Imágen')
    localizacion=models.CharField(max_length=250, verbose_name='Localización')
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Sucursales"

class TelefonoSucursal(models.Model):
    """Clase TelfonoSucursal
    Atributos: numero, sucursal"""
    numero = models.CharField(max_length=100, help_text='Código de área + Nº. Ej.: 351-473-9643.')
    sucursal = models.ForeignKey(Sucursal)
    
    def __unicode__(self):
        return self.numero
    class Meta:
        verbose_name = "Teléfono de Sucursal"
        verbose_name_plural = "Teléfonos de Sucursales"
    
class Empleado(Persona, models.Model):
    """Clase Empleado hereda los atributos de Persona
    Atributos: legajo, turno, sucursal"""
    legajo = models.IntegerField(primary_key=True, unique=True)
    turno = models.ForeignKey(Turno)
    sucursal = models.ForeignKey(Sucursal)  
    
    def __unicode__(self):
        return str(self.legajo)
    
    