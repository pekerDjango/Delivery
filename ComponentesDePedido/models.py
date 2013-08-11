#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TipoIngrediente(models.Model):
    """Clase Tipo Ingrediente
    Atributos: IdTipoIngrediente, NombreIngrediente """
    codigoTipoIngrediente = models.IntegerField(primary_key = True, verbose_name = "Código")
    nombreTipoIngrediente = models.CharField(max_length = 50, verbose_name = "Nombre")
    
    def __unicode__(self):
        return self.nombreTipoIngrediente
    
class Version(models.Model):
    """Clase Version
    Atributos: Clasificacion, codigo, nombre. """
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombre
    
    
class Clasificacion(models.Model):
    """Clase clasificacion: 
    Atributos: Nombre, Descripcion """
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 50)
    version = models.ForeignKey(Version)
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

    

    
class Ingrediente(models.Model):
    
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    precio = models.DecimalField(max_digits = 5, decimal_places = 2 )
    stockActual = models.IntegerField(verbose_name = "Stock Actual")
    stockMinimo = models.IntegerField(verbose_name = "Stock Mínimo")
    tipoIngrediente = models.ForeignKey (TipoIngrediente, verbose_name = "Tipo de ingrediente")
    unidadDeMedida = models.ForeignKey(UnidadDeMedida, verbose_name = "Unidad de Medida")
    
    def __unicode__(self):
        return self.nombre


class Producto (models.Model):
    
    codigo = models.IntegerField (primary_key = True)
    nombre = models.CharField (max_length = 50)
    tiempoPreparacion = models.IntegerField (max_length = 10, verbose_name = "Tiempo Preparacion estimado(minutos)")
    tipoProducto = models.ForeignKey(TipoProducto, verbose_name = "Tipo de Producto")
    version = models.ForeignKey(Version)
    unidadDeMedida = models.ForeignKey (UnidadDeMedida, verbose_name =  "Unidad de Medida")
    
    def __unicode__(self):
        return self.nombre

    
class DetalleIngredientes(models.Model):
   
    tipoIngrediente = models.ForeignKey(TipoIngrediente, verbose_name = "Tipo de Ingrediente")
    ingrediente = models.ForeignKey(Ingrediente)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto)
    def __unicode__(self):
        return str(self.cantidad)
    


    
class DetalleVersiones(models.Model):
    """Clase DetalleVersiones
    Atributos: Clasificacion, Imagen de producto, Precio """
    clasificacion = models.ForeignKey(Clasificacion)
    imagenProducto = models.ImageField(upload_to='imagenes', verbose_name='Im�gen Producto')
    precio = models.DecimalField(max_digits = 5, decimal_places = 2)
    producto = models.ForeignKey(Producto)
    def __unicode__(self):
        return str(self.precio) 
    
    
class Menu (models.Model):
    codigo = models.IntegerField (primary_key = True)
    nombre = models.CharField (max_length = 50)
    detalle = models.CharField(max_length = 200)
    precioVenta = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Precio de venta")
    
    def __unicode__(self):
        return self.nombre
    

class DetalleMenu (models.Model):
    cantidad = models.IntegerField ()
    producto = models.ForeignKey (Producto)
    menu = models.ForeignKey(Menu)
    
    def __unicode__(self):
        return str(self.cantidad)
    
    
class Frecuencia (models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    
    
class Programacion (models.Model):
    diaSemana = models.IntegerField (verbose_name = "Dia de la semana")
    fechaDesde = models.DateTimeField(verbose_name = "Fecha desde")
    fechaHasta = models.DateTimeField(verbose_name = "Fecha Hasta")
    horaDesde = models.TimeField(verbose_name = "Hora desde")
    horaHasta = models.TimeField(verbose_name = "Hora hasta")
    
    def __unicode__(self):
        return str(self.fechaDesde) + str(self.fechaHasta)
    
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
    producto = models.ForeignKey(Producto)
    menu = models.ForeignKey(Menu)
    cantidad = models.IntegerField ()
