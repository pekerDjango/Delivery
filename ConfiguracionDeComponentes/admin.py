#encoding:utf-8
from ConfiguracionDeComponentes.models import Cliente, ExUserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#admin.site.register(Usuario, UserAdmin)

    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono_particular', 'telefono_domicilio', 'apellidos', 'email', 'fecha_nacimiento', 'sexo', 'ofertasYPromocionesDisponibles',)
    fieldsets = (
                 ('Información Personal', {'fields': ('nombre', 'telefono_particular', 'telefono_domicilio', 'apellidos', 'fecha_nacimiento', 'sexo',)}),
                 ('Domicilio Actual', {'fields': ('direccion', 'numero_direccion', 'piso','depto', 'codigo_postal', 'localidad', 'barrio', )}),
                 ('Datos de la cuenta', {'fields': ('ofertasYPromocionesDisponibles','menuDiario', 'notificacionPedidosConfirmados', 'estadoPedidosRealizados',  )}),
                 )

admin.site.register(Cliente, ClienteAdmin)

class ExUserAdmin(admin.ModelAdmin):
    model = ExUserProfile
    
admin.site.register(ExUserProfile, ExUserAdmin)