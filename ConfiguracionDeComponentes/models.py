#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser, PermissionsMixin)
from RecursosDeEmpresa.models import Empleado, Localidad, Barrio
from PedidoRegistrado.models import DomicilioSearch
    
class Cliente(models.Model):
    #username = models.CharField(unique=True,max_length=100,verbose_name="Usuario")
    sexo_choise= (
                  ('F','Femenino'),
                  ('M','Masculino'),
                  )
    nombre = models.CharField(max_length="30",)
    telefono_particular = models.CharField(max_length=100, help_text='Código de área + Nº. Ej.: 351-473-9643.', verbose_name="Teléfono Particular")
    telefono_domicilio =models.CharField(max_length=100, blank=True, null=True, help_text='Código de área + Nº. Ej.: 351-473-9643.', verbose_name="Teléfono Domicilio")
    apellidos = models.CharField(max_length="100")
    email = models.EmailField(unique=True,verbose_name="Correo Electronico")
    fecha_nacimiento = models.DateField()
    sexo =  models.CharField(max_length=1, choices=sexo_choise)
    """
    Datos del domicilio
    """
    direccion = models.CharField(max_length=250, verbose_name='Dirección')
    numero_direccion = models.IntegerField(verbose_name='Número')
    piso = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=50, blank=True, null=True)
    codigo_postal = models.CharField(max_length=100, verbose_name="Código Postal")   
    localidad = models.ForeignKey(Localidad)
    barrio = models.ForeignKey(Barrio)
   
    """
    Datos de interes
    """
    ofertasYPromocionesDisponibles = models.BooleanField(verbose_name = "Ofertas y Promociones disponibles")
    menuDiario= models.BooleanField(verbose_name = "Menú diario")
    notificacionPedidosConfirmados = models.BooleanField(verbose_name = "Notificación de pedidos Confirmados")
    estadoPedidosRealizados = models.BooleanField(verbose_name = "Estado de Pedidos realizados")
    usuario = models.OneToOneField(User, related_name = "Usuario Asociado")
    def __unicode__(self):
        return self.email
    
class ExUserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_human = models.BooleanField()
 
    def __unicode__(self):
        return self.user

from registration.signals import user_registered
 
def user_registered_callback(sender, user, request, **kwargs):
    profile = ExUserProfile(user = user)
    profile.is_human = bool(request.POST["is_human"])
    profile.save()
 
user_registered.connect(user_registered_callback)