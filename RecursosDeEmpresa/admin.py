from RecursosDeEmpresa.models import Empleado, Sucursal, TipoDocumento, Barrio, Localidad, TelefonoPersona, TelefonoSucursal, Turno, CalificacionServicio, Provincia 
from django.contrib import admin
admin.site.register(Empleado)
admin.site.register(Sucursal)
admin.site.register(TipoDocumento)
admin.site.register(Barrio)
admin.site.register(Localidad)
admin.site.register(Provincia)
#admin.site.register(TelefonoPersona)
admin.site.register(Turno)
admin.site.register(CalificacionServicio)
admin.site.register(TelefonoSucursal)