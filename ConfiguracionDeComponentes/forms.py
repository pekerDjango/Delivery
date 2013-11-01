#encoding:utf-8
from django import forms
from ConfiguracionDeComponentes.models import Cliente, ExUserProfile
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from RecursosDeEmpresa.models import Localidad, Barrio

class ClienteForm(forms.ModelForm):
    class Meta: 
        model = Cliente

from registration.forms import RegistrationForm
 
class ExRegistrationForm(RegistrationForm):
    sexo_choise= (
                  ('F','Femenino'),
                  ('M','Masculino'),
                  )
    nombre = forms.CharField()
    apellidos = forms.CharField()
    telefono_particular = forms.CharField(help_text='Código de área + Nº. Ej.: 351-473-9643.')
    telefono_domicilio =forms.CharField(help_text='Código de área + Nº. Ej.: 351-473-9643.')
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    sexo =  forms.CharField(widget = forms.Select(choices= sexo_choise ))
    direccion = forms.CharField(max_length=250)
    numero_direccion = forms.IntegerField()
    piso = forms.IntegerField()
    depto = forms.CharField(max_length=50)
    codigo_postal = forms.CharField(max_length=100)   
    localidades = Localidad.objects.all().values_list()
    localidad = forms.CharField(widget = forms.Select(choices= localidades))
    barrios =  Barrio.objects.all().values_list()
    barrio = forms.CharField(widget = forms.Select(choices=barrios))
    ofertasYPromocionesDisponibles = forms.BooleanField(initial=True, required=False)
    menuDiario= forms.BooleanField(initial=True, required=False)
    notificacionPedidosConfirmados = forms.BooleanField(initial=True, required=False)
    estadoPedidosRealizados = forms.BooleanField(initial=True, required=False)
    
    
    