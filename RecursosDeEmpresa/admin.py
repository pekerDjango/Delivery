from RecursosDeEmpresa.models import Empleado, Sucursal, TipoDocumento, Barrio, Localidad, TelefonoPersona, TelefonoSucursal, Turno, CalificacionServicio, Provincia 
from django.contrib import admin
from django_admin_bootstrapped.admin.models import SortableInline

class TelefonoSucursalInLine(admin.StackedInline, SortableInline):
    model = TelefonoSucursal
    verbose_name_plural = "Telefonos de Sucursales"
    extra = 1

class SucursalAdmin(admin.ModelAdmin):
    inlines = [TelefonoSucursalInLine,]
    list_display=('codigo', 'nombre', 'direccion', 'barrio', 'Vista_Previa')
    list_filter=('codigo', 'nombre', 'direccion', 'barrio')
    ordering=('nombre',)
    search_fields=('codigo','nombre','barrio__nombre','localidad__nombre')
    
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('legajo','nombre','apellido')
    list_filter=('legajo','apellido')
    ordering=('legajo',)
    search_fields=('legajo','nombre','apellido','numero_documento')
    
class BarrioAdmin(admin.ModelAdmin): 
    ordering=('nombre',)
    search_fields=('nombre',)
    
class CalificacionServicioAdmin(admin.ModelAdmin):
    list_display=('nombre', 'descripcion')
    list_filter=('nombre',)
    ordering=('nombre',)
    search_fields=('nombre',)
    
class LocalidadAdmin(admin.ModelAdmin): 
    ordering=('nombre',)
    search_fields=('nombre',)
    
class TipoDocumentoAdmin(admin.ModelAdmin): 
    ordering=('nombre',)
    search_fields=('nombre',)
    
class ProvinciaAdmin(admin.ModelAdmin): 
    ordering=('nombre',)
    search_fields=('nombre',)
    
class TurnoAdmin(admin.ModelAdmin):
    list_display=('codigo', 'descripcion')
    list_filter=('codigo','descripcion') 
    ordering=('codigo',)
    search_fields=('codigo','descripcion')
    
class TelefonoSucursalAdmin(admin.ModelAdmin):
    list_display=('numero', )
    list_filter=('sucursal__nombre',) 
    search_fields=('numero','sucursal__nombre')

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
#admin.site.register(TelefonoPersona)
admin.site.register(Turno, TurnoAdmin)
admin.site.register(CalificacionServicio, CalificacionServicioAdmin)
admin.site.register(TelefonoSucursal, TelefonoSucursalAdmin)