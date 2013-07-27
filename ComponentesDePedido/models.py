#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TipoIngrediente(models.Model):
    """Clase Tipo Ingrediente
    Atributos: IdTipoIngrediente, NombreIngrediente """
    codigoTipoIngrediente = models.IntegerField(primary_key = True)
    nombreTipoIngrediente = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombreTipoIngrediente
    
class Clasificacion(models.Model):
    """Clase clasificacion: 
    Atributos: Nombre, Descripcion """
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombre
    
class UnidadDeMedida(models.Model):
    """Clase Unidad de medida:
    Atributos: Codigo, Descripcion. """
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombre
    
class TipoProducto(models.Model):
    """Clase TipoProducto 
    Atributos: C�digoTipoProducto, Nombre """
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombre

    
class Version(models.Model):
    """Clase Version
    Atributos: Clasificacion, codigo, nombre. """
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombre
    
class Ingrediente(models.Model):
    
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    precio = models.DecimalField(max_digits = 3, decimal_places = 2 )
    stockActual = models.IntegerField()
    stockMinimo = models.IntegerField()
    tipoIngrediente = models.ForeignKey (TipoIngrediente)
    unidadDeMedida = models.ForeignKey(UnidadDeMedida)
    
    def __unicode__(self):
        return self.nombre
    
class DetalleIngredientes(models.Model):
    ingrediente = models.ForeignKey(Ingrediente)
    tipoIngrediente = models.ForeignKey(TipoIngrediente)
    cantidad = models.IntegerField()
    
    def __unicode__(self):
        return self.ingrediente + self.cantidad
    
class Producto (models.Model):
    
    codigo = models.IntegerField (primary_key = True)
    nombre = models.CharField (max_length = 50)
    tiempoPreparacion = models.IntegerField (max_length = 10, verbose_name = "Tiempo Preparacion estimado(minutos)")
    tipoProducto = models.ForeignKey(TipoProducto)
    version = models.ForeignKey(Version)
    unidadDeMedida = models.ForeignKey (UnidadDeMedida)
    
    def __unicode__(self):
        return self.nombre

    
class DetalleVersiones(models.Model):
    """Clase DetalleVersiones
    Atributos: Clasificacion, Imagen de producto, Precio """
    clasificacion = models.ForeignKey(Clasificacion)
    imagenProducto = models.ImageField(upload_to='/imagenes', verbose_name='Im�gen Producto')
    precio = models.DecimalField(max_digits = 3, decimal_places = 2)
    producto = models.ForeignKey(Producto)
    def __unicode__(self):
        return self.clasificacion 
    
    
class Menu (models.Model):
    codigo = models.IntegerField (primary_key = True)
    nombre = models.CharField (max_length = 50)
    detalle = models.CharField(max_length = 200)
    precioVenta = models.DecimalField(max_digits = 3, decimal_places = 2)
    
    def __unicode__(self):
        return self.nombre
    

class DetalleMenu (models.Model):
    cantidad = models.IntegerField ()
    producto = models.OneToOneField (Producto)
    menu = models.ForeignKey(Menu)
    
    def __unicode__(self):
        return self.menu + self.producto
    
    
class Frecuencia (models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    
    
class Programacion (models.Model):
    diaSemana = models.IntegerField ()
    fechaDesde = models.DateTimeField()
    fechaHasta = models.DateTimeField()
    horaDesde = models.TimeField()
    horaHasta = models.TimeField()
    
    def __unicode__(self):
        return self.fechaDesde + self.fechaHasta
    
class Promocion (models.Model):
    codigo = codigo = models.IntegerField ( primary_key = True)
    nombre = models.CharField (max_length = 50)
    imagenProducto = models.ImageField(upload_to='/imagenes', verbose_name='Im�gen Promocion')
    precio = models.DecimalField(max_digits = 3, decimal_places = 2)
    stock = models.IntegerField ( )
    tiempoPreparacion = models.IntegerField(verbose_name = 'Tiempo estimado de preparaci�n(Minutos)')
    programacion = models.ForeignKey(Programacion)
    
    def __unicode__(self):
        return self.nombre
    
class DetallePromocion (models.Model):
    promocion = models.ForeignKey(Promocion)
    producto = models.OneToOneField(Producto)
    menu = models.OneToOneField(Menu)
    cantidad = models.IntegerField ()
