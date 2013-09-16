#encoding:utf-8
from django.db import models
# Create your models here.

class TipoIngrediente(models.Model):
    """Clase Tipo Ingrediente
    Atributos: IdTipoIngrediente, NombreIngrediente """
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField(max_length = 50, verbose_name = "Nombre")
    
    def __unicode__(self):
        return self.nombre
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
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField(max_length = 50)
    clasificacion = models.ManyToManyField(Clasificacion)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name = "Versión"
        verbose_name_plural = "Versiones"   
    
class UnidadDeMedida(models.Model):
    """Clase Unidad de medida:
    Atributos: Codigo, Descripcion. """
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Unidades de medida"
    
class TipoProducto(models.Model):
    """Clase TipoProducto 
    Atributos: CódigoTipoProducto, Nombre,Imagen """
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField(max_length = 50)
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Vista Previa')
    
    def __unicode__(self):
        return self.nombre
    def Vista_Previa(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)
    
    Vista_Previa.allow_tags = True
    class Meta:
        verbose_name_plural = "Tipos de Productos" 
    
class Ingrediente(models.Model):        
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField(max_length = 50)
    tipoIngrediente = models.ForeignKey (TipoIngrediente, verbose_name = "Tipo de ingrediente")
    unidadDeMedida = models.ForeignKey(UnidadDeMedida, verbose_name = "Unidad de Medida")
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Vista Previa')
    stockActual = models.IntegerField(verbose_name = "Stock Actual")
    stockMinimo = models.IntegerField(verbose_name = "Stock Mínimo")
    stockCorte = models.IntegerField(verbose_name = "Stock Corte")
    precio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Precio($)" )
        
    def __unicode__(self):
        return self.nombre

class Producto (models.Model):    
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField (max_length = 50)
    tiempoPreparacion = models.IntegerField (max_length = 10, verbose_name = "Tiempo Preparacion estimado(minutos)")
    tipoProducto = models.ForeignKey(TipoProducto, verbose_name = "Tipo de Producto")
    version = models.ForeignKey(Version)
    estado = models.BooleanField(default=True) 
    
    def __unicode__(self):
        return self.nombre
    def getDetalleVersiones(self):
        return DetalleVersiones.objects.filter(producto=self)
    
class DetalleIngredientes(models.Model):
   
    tipoIngrediente = models.ForeignKey(TipoIngrediente, verbose_name = "Tipo de Ingrediente")
    ingrediente = models.ForeignKey(Ingrediente)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    def __unicode__(self):
        return u'%s- %s' % (self.producto.nombre, self.ingrediente.nombre) 
 
    class Meta:
        verbose_name_plural = "Detalle de ingredientes"
    
class DetalleVersiones(models.Model):
    """Clase DetalleVersiones
    Atributos: Clasificacion, Imagen de producto, Precio """
    clasificacion = models.ForeignKey(Clasificacion)
    imagenProducto = models.ImageField(upload_to='imagenes', verbose_name='Imágen Producto')
    precio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Precio($)")
    producto = models.ForeignKey(Producto)
    def __unicode__(self):
        return u'%s- %s'%(self.producto.nombre, self.clasificacion.nombre)
    class Meta:
        verbose_name_plural = "Detalle de versiones"
    
class Menu (models.Model):
    def Vista_Previa(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)
    
    Vista_Previa.allow_tags = True
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField (max_length = 50, verbose_name = "Nombre Menú")
    precioVenta = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Precio($)")
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Vista Previa')
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name='Menú'
        verbose_name_plural = "Menús"

class DetalleMenu (models.Model):
    menu = models.ForeignKey(Menu)
    tipoProducto = models.ForeignKey(TipoProducto)
    producto = models.ForeignKey (Producto)
    versionProducto = models.ForeignKey(Clasificacion, verbose_name = "Versiones de Producto ")
    
    cantidad = models.IntegerField ()
    
    def __unicode__(self):
        return u'%s, %s'%(self.menu.nombre, self.producto.nombre)
    
    class Meta:
        verbose_name="Detalle de Menú"
        verbose_name_plural = "Detalles de Menú"
    
class Frecuencia (models.Model):
    descripcion = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.descripcion
        
class Promocion (models.Model):
    def Vista_Previa(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)
    
    Vista_Previa.allow_tags = True
    codigo = models.AutoField(primary_key=True, verbose_name = "Código")
    nombre = models.CharField (max_length = 50)
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to="imagenes", verbose_name="Imágen Promocion")
    precio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name ="Precio($)")
    stock = models.IntegerField (blank=True, null=True)
    tiempoPreparacion = models.IntegerField(verbose_name = "Tiempo estimado de preparación(Minutos)")
    estado = models.BooleanField(default=True)    
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name = "Promoción"
        verbose_name_plural = "Promociones"
        
class DiaSemana(models.Model):
    nombre = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.nombre
        
class Programacion (models.Model):
#    frecuencia = models.ForeignKey(Frecuencia, default="Seleccione la Frecuencia")
#    lunes = models.BooleanField()
#    martes = models.BooleanField()
#    miercoles = models.BooleanField(verbose_name='Miércoles')
#    jueves = models.BooleanField()
#    viernes = models.BooleanField()
#    sabado = models.BooleanField()
#    domingo = models.BooleanField()
    diaSemana = models.ManyToManyField(DiaSemana, verbose_name="Dias de la semana")
    fechaDesde = models.DateField(verbose_name = "Fecha desde")
    fechaHasta = models.DateField(verbose_name = "Fecha Hasta")
    horaDesde = models.TimeField(verbose_name = "Hora desde", help_text="Formato 24hs")
    horaHasta = models.TimeField(verbose_name = "Hora hasta", help_text="Formato 24hs")
    promocion = models.ForeignKey(Promocion)
    
    def __unicode__(self):
        return  u'Desde: %s Hasta: %s'%(self.fechaDesde, self.fechaHasta)
    class Meta:
        verbose_name_plural = "Programaciones"
        
class DetallePromocionProducto(models.Model):
    promocion = models.ForeignKey(Promocion)
    tipoProducto = models.ForeignKey(TipoProducto, verbose_name = 'Tipo de Producto')    
    producto = models.ForeignKey(Producto)
    versionProducto = models.ForeignKey(Clasificacion, verbose_name = "Versiones de Producto")
    cantidad = models.IntegerField ()
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos Componentes"
    
class DetallePromocionMenu(models.Model):
    promocion = models.ForeignKey(Promocion)
    menu = models.ForeignKey(Menu)
    cantidad = models.IntegerField ()
    
    class Meta:
        verbose_name = "Menú"
        verbose_name_plural = "Menus Componentes"