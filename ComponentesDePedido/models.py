#encoding:utf-8
from django.db import models
# Create your models here.

class TipoIngrediente(models.Model):
    """Clase Tipo Ingrediente
    Atributos: IdTipoIngrediente, NombreIngrediente """
    codigoTipoIngrediente = models.IntegerField(primary_key = True, verbose_name = "Código")
    nombreTipoIngrediente = models.CharField(max_length = 50, verbose_name = "Nombre")
    
    def __unicode__(self):
        return self.nombreTipoIngrediente
    class Meta:
        verbose_name_plural = "Tipos de Ingredientes"
    
class Clasificacion(models.Model):
    """Clase clasificacion: 
    Atributos: Nombre, Descripcion """
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Clasificaciones"
    
class Version(models.Model):
    """Clase Version
    Atributos: Clasificacion, codigo, nombre. """
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    clasificacion = models.ManyToManyField(Clasificacion)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Versiones"
    

    
class UnidadDeMedida(models.Model):
    """Clase Unidad de medida:
    Atributos: Codigo, Descripcion. """
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Unidades de medida"
    
class TipoProducto(models.Model):
    """Clase TipoProducto 
    Atributos: CódigoTipoProducto, Nombre """
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipos de Productos"
    

    
class Ingrediente(models.Model):
    
    codigo = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    tipoIngrediente = models.ForeignKey (TipoIngrediente, verbose_name = "Tipo de ingrediente")
    unidadDeMedida = models.ForeignKey(UnidadDeMedida, verbose_name = "Unidad de Medida")
    stockActual = models.IntegerField(verbose_name = "Stock Actual")
    stockMinimo = models.IntegerField(verbose_name = "Stock Mínimo")
    precio = models.DecimalField(max_digits = 5, decimal_places = 2 )
    
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
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    def __unicode__(self):
        return u'%s, %s' % (self.producto.nombre, self.ingrediente.nombre) 
 
    class Meta:
        verbose_name_plural = "Detalle de ingredientes"

    
class DetalleVersiones(models.Model):
    """Clase DetalleVersiones
    Atributos: Clasificacion, Imagen de producto, Precio """
    clasificacion = models.ForeignKey(Clasificacion)
    imagenProducto = models.ImageField(upload_to='imagenes', verbose_name='Imágen Producto')
    precio = models.DecimalField(max_digits = 5, decimal_places = 2)
    producto = models.ForeignKey(Producto)
    def __unicode__(self):
        return str(self.precio) 
    class Meta:
        verbose_name_plural = "Detalle de versiones"
    
class Menu (models.Model):
    codigo = models.IntegerField (primary_key = True)
    nombre = models.CharField (max_length = 50)
    precioVenta = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Precio de venta")
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Vista Previa')
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Menu"

class DetalleMenu (models.Model):
    menu = models.ForeignKey(Menu)
    tipoProducto = models.ForeignKey(TipoProducto)
    producto = models.ForeignKey (Producto)
    cantidad = models.IntegerField ()
    
    def __unicode__(self):
        return u'%s, %s'%(self.menu.nombre, self.producto.nombre)
    
    class Meta:
        verbose_name_plural = "Detalles de Menu"
    
class Frecuencia (models.Model):
    descripcion = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.descripcion
    
class Programacion (models.Model):
    frecuencia = models.ForeignKey(Frecuencia, default="Seleccione la Frecuencia")
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField(verbose_name='Miércoles')
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()
    diaSemana = models.IntegerField (verbose_name = "Dia de la semana")
    fechaDesde = models.DateField(verbose_name = "Fecha desde")
    fechaHasta = models.DateField(verbose_name = "Fecha Hasta")
    horaDesde = models.TimeField(verbose_name = "Hora desde", help_text="Formato 24hs")
    horaHasta = models.TimeField(verbose_name = "Hora hasta", help_text="Formato 24hs")
    
    def __unicode__(self):
        return str(self.frecuencia.descripcion)
    class Meta:
        verbose_name_plural = "Programaciones"
    
class Promocion (models.Model):
    codigo = models.IntegerField ( primary_key = True)
    nombre = models.CharField (max_length = 50)
    imagenProducto = models.ImageField(upload_to='/imagenes', verbose_name='Imágen Promocion')
    precio = models.DecimalField(max_digits = 3, decimal_places = 2)
    stock = models.IntegerField ( )
    tiempoPreparacion = models.IntegerField(verbose_name = 'Tiempo estimado de preparación(Minutos)')
    programacion = models.ForeignKey(Programacion)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Promociones"
        
        
class DetallePromocionProducto(models.Model):
    promocion = models.ForeignKey(Promocion)
    tipoProducto = models.ForeignKey(TipoProducto, verbose_name = 'Tipo de Producto')
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField ()
    
    class Meta:
        verbose_name_plural = "Productos de la Promo"
    
class DetallePromocionMenu(models.Model):
    promocion = models.ForeignKey(Promocion)
    menu = models.ForeignKey(Menu)
    cantidad = models.IntegerField ()
    
    class Meta:
        verbose_name_plural = "Menus de la Promo"