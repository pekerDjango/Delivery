#encoding:utf-8
from ConfiguracionDeComponentes.models import Usuario, Cliente
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ConfiguracionDeComponentes.forms import ClienteCreationForm, ClienteChangeForm
#admin.site.register(Usuario, UserAdmin)

    
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteChangeForm
    add_form = ClienteCreationForm
    list_display = ('nombre', 'telefono_particular', 'telefono_domicilio', 'apellidos', 'email', 'fecha_nacimiento', 'sexo', 'ofertasYPromocionesDisponibles',)
    fieldsets = (
                 ('Información Personal', {'fields': ('nombre', 'telefono_particular', 'telefono_domicilio', 'apellidos', 'fecha_nacimiento', 'sexo',)}),
                 ('Domicilio Actual', {'fields': ('direccion', 'numero_direccion', 'piso','depto', 'codigo_postal', 'localidad', 'barrio', )}),
                 ('Datos de la cuenta', {'fields': ('ofertasYPromocionesDisponibles','menuDiario', 'notificacionPedidosConfirmados', 'estadoPedidosRealizados',  )}),
                 )

admin.site.register(Cliente, ClienteAdmin)