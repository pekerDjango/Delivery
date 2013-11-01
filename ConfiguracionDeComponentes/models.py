#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from RecursosDeEmpresa.models import Localidad, Barrio
from datetime import datetime, date
    
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
    #username = models.CharField(unique=True,max_length=100,verbose_name="Usuario")
    sexo_choise= (
                  ('F','Femenino'),
                  ('M','Masculino'),
                  )
    user = models.ForeignKey(User, unique=True)
    nombre = models.CharField(max_length="30",)
    apellidos = models.CharField(max_length="100")
    telefono_particular = models.CharField(max_length=100, help_text='Código de área + Nº. Ej.: 351-473-9643.', verbose_name="Teléfono Particular")
    telefono_domicilio =models.CharField(max_length=100, blank=True, null=True, help_text='Código de área + Nº. Ej.: 351-473-9643.', verbose_name="Teléfono Domicilio")
    fecha_nacimiento = models.DateField(default = datetime.now())
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
    Datos de Interes
    """
    ofertasYPromocionesDisponibles = models.BooleanField(verbose_name = "Ofertas y Promociones disponibles", default = True)
    menuDiario= models.BooleanField(verbose_name = "Menú diario", default = True)
    notificacionPedidosConfirmados = models.BooleanField(verbose_name = "Notificación de pedidos Confirmados", default = True)
    estadoPedidosRealizados = models.BooleanField(verbose_name = "Estado de Pedidos realizados",default = True)
    #usuario = models.OneToOneField(User, related_name = "Usuario Asociado")
    
    def __unicode__(self):
        return self.user

from registration.signals import user_registered
 
def user_registered_callback(sender, user, request, **kwargs):
    profile = ExUserProfile(user = user)
    profile.nombre = request.POST["nombre"]
    profile.apellidos = request.POST["apellidos"]
    profile.direccion = request.POST["direccion"]
    profile.depto = request.POST["depto"]
    profile.piso = request.POST["piso"]
    profile.barrio = Barrio.objects.get(pk = int(request.POST["barrio"]))
    
    profile.codigo_postal = request.POST["codigo_postal"]
    profile.numero_direccion = request.POST["numero_direccion"]
    profile.sexo = request.POST["sexo"]
    profile.telefono_domicilio = request.POST["telefono_domicilio"]
    profile.telefono_particular = request.POST["telefono_particular"]
    profile.localidad = Localidad.objects.get(pk = int(request.POST["localidad"]))
    profile.fecha_nacimiento = datetime.strptime(request.POST["fecha_nacimiento"], "%d/%m/%Y")
    profile.ofertasYPromocionesDisponibles = bool(request.POST["ofertasYPromocionesDisponibles"])
    profile.menuDiario = bool(request.POST["menuDiario"])
    profile.notificacionPedidosConfirmados = bool(request.POST["notificacionPedidosConfirmados"])
    profile.estadoPedidosRealizados = bool(request.POST["estadoPedidosRealizados"])
    
    profile.save()
 
user_registered.connect(user_registered_callback)