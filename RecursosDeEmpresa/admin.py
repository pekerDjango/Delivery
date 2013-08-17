#encoding:utf-8
from RecursosDeEmpresa.models import Empleado, Sucursal, TipoDocumento, Barrio, Localidad, TelefonoPersona, TelefonoSucursal, Turno, CalificacionServicio, Provincia 
from django.contrib import admin
from django_admin_bootstrapped.admin.models import SortableInline
from django.forms import TextInput, Textarea, Select
from django.db import models
from form_utils.widgets import ImageWidget

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
#    fields =('codigo','nombre',('direccion','numero_direccion','piso','depto'),('codigo_postal','barrio','localidad'), 'calificacion_servicio','imagen')
    fieldsets = (
        (None, {
            'fields': ('codigo', 'nombre', 'calificacion_servicio','imagen')
        }),
        ('Dirección', {
            'classes': ('wide','extrapretty'),
            'fields': (('direccion','numero_direccion','codigo_postal'),('barrio','localidad'))
        }),
                 )
    readonly_fields =('codigo',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget}
      
    }
    
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('legajo','nombre','apellido','numero_documento')
    list_filter=('legajo','apellido')
    ordering=('legajo','nombre', 'apellido')
    search_fields=('legajo','nombre','apellido','numero_documento')
    fieldsets = (
        (None, {
            'fields': ('legajo', 'nombre', 'apellido','sexo', 'email','tipo_documento','numero_documento','telefono_particular','telefono_domicilio','turno','sucursal')
        }),
        ('Dirección', {
            'classes': ('wide','extrapretty'),
            'fields': (('direccion','numero_direccion','piso'),('depto','codigo_postal'),('provincia','localidad','barrio'))
        }),
                 )
#    readonly_fields =('legajo',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},      
    }
    
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
    fields =('codigo','descripcion')
    readonly_fields =('codigo',)
    
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