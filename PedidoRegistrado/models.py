#encoding:utf-8
from django.db import models
from RecursosDeEmpresa.models import Localidad, Barrio
from django.contrib.auth.models import User
from ComponentesDePedido.models import Producto

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
#    usuario = models.OneToOneField(User)  
    def __unicode__(self):
        return self.nombre + self.apellido

class EstadoPedido(models.Model):
    """Clase Estado Pedido
    Atributos:nombre, descripcion"""
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
        
class Pedido(models.Model):
    """Clase Pedido 
    Atributos:cliente, fechaPedido, hora_entrega, estado, servicio, tipologia_vivienda, precio_envio, precio_total"""
    cliente = models.ForeignKey(Cliente)
    fechaPedido = models.DateField()
    hora_entrega = models.TimeField()
    estado = models.ForeignKey(EstadoPedido)
    servicio = models.ForeignKey(Servicio)
    tipologia_vivienda = models.ForeignKey(TipologiaVivienda)
    precio_envio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Costo de Envio($)" )
    precio_total = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Total($)" )
    
class EstadoDetallePedido(models.Model):
    """Clase Estado de Detalle Pedido
    Atributos:nombre, descripcion"""
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    
class DetallePedido(models.Model):
    """Clase Detalle de Pedido
    Atributos: pedido, cantidad, producto, estado, precio"""
    pedido = models.ForeignKey(Pedido)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto)
    estado = models.ForeignKey(EstadoDetallePedido)
    precio = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Precio($)" )
    
    
    
    
        
    