#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser, PermissionsMixin)
from RecursosDeEmpresa.models import Empleado, Localidad, Barrio
from PedidoRegistrado.models import DomicilioSearch

class ClienteManager(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise ValueError('El Cliente debe tener un nombre de usuario')
        if not password:
            raise ValueError('La contraseña no es valida')
        user = self.model(
            username = email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,password):
        if not username:
            raise ValueError('El Cliente debe tener un nombre de usuario')
        if not password:
            raise ValueError('La contraseña no es valida')
        user = self.model(
            username = username
        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    def get_by_natural_key(self, email):
        return self.get(username=email)




class Usuario (User):
    empleado = models.OneToOneField(Empleado)
    
class Cliente(AbstractBaseUser,PermissionsMixin):
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
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = ClienteManager()
    """
    Datos de interes
    """
    ofertasYPromocionesDisponibles = models.BooleanField(verbose_name = "Ofertas y Promociones disponibles")
    menuDiario= models.BooleanField(verbose_name = "Menú diario")
    notificacionPedidosConfirmados = models.BooleanField(verbose_name = "Notificación de pedidos Confirmados")
    estadoPedidosRealizados = models.BooleanField(verbose_name = "Estado de Pedidos realizados")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return "%s %s"%(self.nombre, self.apellidos)

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perms(self):
        return True

    def has_module_perms(self):
        return True

    def is_staff(self):
        return self.is_superuser