from RecursosDeEmpresa.models import Empleado, Sucursal, TipoDocumento, Barrio, Localidad, TelefonoPersona, TelefonoSucursal, Turno, CalificacionServicio, Provincia 
from django.contrib import admin

class EmpleadoAdmin(admin.ModelAdmin):
    campos=(('nombre , apellido'),('tipo_documento' , 'numero_documento'))

class PersonAdmin(admin.ModelAdmin):
    raw_id_fields = ('telefono_particular'),

admin.site.register(Empleado, PersonAdmin)
admin.site.register(Sucursal)
admin.site.register(TipoDocumento)
admin.site.register(Barrio)
admin.site.register(Localidad)
admin.site.register(Provincia)
admin.site.register(TelefonoPersona)
admin.site.register(Turno)
admin.site.register(CalificacionServicio)
admin.site.register(TelefonoSucursal)