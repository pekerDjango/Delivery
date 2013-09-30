#encoding:utf-8
from django.db import models
from RecursosDeEmpresa.models import Localidad, Barrio
from django.contrib.auth.models import User
from ComponentesDePedido.models import DetalleVersiones, Menu, Promocion, TipoProducto, Version, Clasificacion, TipoIngrediente, Ingrediente

class Servicio(models.Model):
    """Clase Servicio
    Atributos:nombre, descripcion, imagen"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Imágen')
    
    def __unicode__(self):
        return self.nombre
    
    def Vista_Previa(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)    
    
    Vista_Previa.allow_tags = True

class TipologiaVivienda(models.Model):
    """Clase Tipologia Vivienda
    Atributos:nombre, imagen"""
    nombre = models.CharField(max_length=100)  
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Imágen')
    
    def __unicode__(self):
        return self.nombre
    
    def Vista_Previa(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)    
    
    Vista_Previa.allow_tags = True
    
class DomicilioSearch(models.Model):
    """Clase DomicilioSearch
    Atributos: direccion,numero_direccion,piso,depto,codigo_postal,localidad,barrio"""
    direccion = models.CharField(max_length=250, verbose_name='Dirección')
    numero_direccion = models.IntegerField(verbose_name='Número')
    piso = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=50, blank=True, null=True)
    codigo_postal = models.CharField(max_length=100, verbose_name="Código Postal")   
    localidad = models.ForeignKey(Localidad)
    barrio = models.ForeignKey(Barrio)    
    def __unicode__(self):
        return self.direccion + str(self.numero_direccion)
    class Meta:
        verbose_name="Domicilio Cliente"        
        verbose_name_plural = "Domicilios"

class Cliente(models.Model):
    """Clase Cliente
    Atributos:nombre, apellido, sexo, email, telefono_particular"""
    sexo_choise= (
                  ('F','Femenino'),
                  ('M','Masculino'),
                  )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo =  models.CharField(max_length=1, choices=sexo_choise)
    email = models.EmailField(max_length=50, help_text='to@example.com')
    telefono_particular = models.CharField(max_length=100, help_text='Código de área + Nº. Ej.: 351-473-9643.', verbose_name="Teléfono Particular")
    usuario = models.OneToOneField(User)  
    def __unicode__(self):
        return u'%s, %s'%(self.nombre, self.apellido)

class EstadoPedido(models.Model):
    """Clase Estado Pedido
    Atributos:nombre, descripcion"""
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class Pedido(models.Model):
    """Clase Pedido 
    Atributos:cliente, fechaPedido, hora_entrega, estado, servicio, tipologia_vivienda, precio_envio, precio_total"""
    cliente = models.ForeignKey(Cliente)
    fechaPedido = models.DateTimeField()
    hora_entrega = models.TimeField(blank=True, null=True)
    estado = models.ForeignKey(EstadoPedido)
    servicio = models.ForeignKey(Servicio)
    tipologia_vivienda = models.ForeignKey(TipologiaVivienda)
    precio_envio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Costo de Envio($)" )    
    def __unicode__(self):
        return str(self.fechaPedido)
    def subTotal(self):
        total = 0
        for d in self.getDetallePedido():
            total += float(d.precio) * float(d.cantidad)
        return total
    def precioTotal(self):
        total = float(self.subTotal()) + float(self.precio_envio)        
        return total
    def cantidadTotalProductos(self):
        total = 0
        for d in self.getDetallePedido():
            total +=  d.cantidad
        return total
    def getDetallePedido(self):
        return DetallePedido.objects.filter(pedido=self)                   
    
class DetallePedido(models.Model):
    """Clase Detalle de Pedido
    Atributos: pedido, cantidad, producto,menu, estado, precio"""
    pedido = models.ForeignKey(Pedido)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(DetalleVersiones,blank=True, null=True)
    menu = models.ForeignKey(Menu, blank=True, null=True)
    promocion = models.ForeignKey(Promocion, blank=True, null=True)
    precio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Precio($)" )    
    def __unicode__(self):
        return u'%s, %s'%(self.pedido.nombre)   
    def precioTotalUnidad(self):
        total = (self.precio * self.cantidad)
        return total
    
class ProductoParaArmar(models.Model):
    """Clase Producto para Armar""
    Atributos: tipo producto, slogan y version"""
    tipo_producto = models.ForeignKey(TipoProducto, verbose_name = "Tipo de Producto")
    slogan = models.CharField(max_length=50, verbose_name="Slogan Producto")
    version = models.ForeignKey(Version)
    def __unicode__(self):
        return self.slogan
    class Meta:
        verbose_name_plural = "Productos para armar"
    
class DetalleVersiones(models.Model):
    """Clase DetalleVersiones
    Atributos: Clasificacion, Imagen de producto, Precio """
    clasificacion = models.ForeignKey(Clasificacion, related_name="%(app_label)s_%(class)s_related")
#    imagenProducto = models.ImageField(upload_to='imagenes', verbose_name='Imágen Producto')
    precio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Precio por clasificación($)")
    producto = models.ForeignKey(ProductoParaArmar)
    def __unicode__(self):
        return u'%s- %s'%(self.producto.slogan, self.clasificacion.nombre)
    class Meta:
        verbose_name_plural = "Detalle de versiones"
        
class SeccionProducto(models.Model):
    """ Clase Seccion por producto
    Atributos: producto, nombre, orden, tipo ingrediente, descripcion, 
    obligatoria, excluyente, cantidad de exclusiones"""
    producto = models.ForeignKey(ProductoParaArmar)
    nombre = models.CharField(max_length=100, verbose_name="Sección Producto")
    orden = models.IntegerField(verbose_name="Orden Presentación")
    tipoIngrediente = models.ForeignKey(TipoIngrediente, verbose_name = "Tipo de Ingrediente")
    descripcion = models.CharField(max_length = 50)
    obligatoria = models.BooleanField(verbose_name = "Sección Obligatoria")
    excluyente = models.BooleanField(verbose_name = "Clasifiaciones Excluyentes")
    cantidad_exclusiones = models.IntegerField(verbose_name = "Cantidad Exclusiones")
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Secciones del Producto"
        
class IngredientesSeccion(models.Model):
    """ Clase Ingredientes por seccion
    Atributos: producto, ingredientes, clasificacion, cantidad"""
    producto = models.ForeignKey(ProductoParaArmar)
    ingrediente = models.ForeignKey(Ingrediente)
    clasificacion = models.ForeignKey(Clasificacion)
    cantidad = models.IntegerField()
    def __unicode__(self):
        return self.seccion.nombre + self.ingrediente.nombre
    class Meta:
        verbose_name_plural = "Ingredientes por Seccion"
  
    
    
    
        
    