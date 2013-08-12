from RecursosDeEmpresa.models import Empleado, Sucursal, TipoDocumento, Barrio, Localidad, TelefonoPersona, TelefonoSucursal, Turno, CalificacionServicio, Provincia 
from django.contrib import admin
from django_admin_bootstrapped.admin.models import SortableInline

class TelefonoSucursalInLine(admin.StackedInline, SortableInline):
    model = TelefonoSucursal
    verbose_name_plural = "Telefonos de Sucursales"
    extra = 1

class SucursalAdmin(admin.ModelAdmin):
    inlines = [TelefonoSucursalInLine,]
    
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('legajo','nombre','apellido')
    list_filter=('legajo','apellido')
    ordering=('legajo',)
    search_fields=('legajo','nombre','apellido','numero_documento')

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(TipoDocumento)
admin.site.register(Barrio)
admin.site.register(Localidad)
admin.site.register(Provincia)
#admin.site.register(TelefonoPersona)
admin.site.register(Turno)
admin.site.register(CalificacionServicio)
admin.site.register(TelefonoSucursal)