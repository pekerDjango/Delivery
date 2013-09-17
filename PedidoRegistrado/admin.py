from django.contrib import admin
from PedidoRegistrado.models import Servicio, TipologiaVivienda, DomicilioSearch, Cliente, EstadoPedido, Pedido, DetallePedido
from form_utils.widgets import ImageWidget
from django.db import models
from django.forms import TextInput, Textarea
from django_admin_bootstrapped.admin.models import SortableInline

class ServicioAdmin(admin.ModelAdmin):

        search_fields = ('nombre', 'descripcion')
        list_display = ('nombre', 'descripcion')
        list_filter = ('nombre', )
        ordering=('nombre',)
        fields =('nombre','descripcion')   
        formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }
    
class TipologiaViviendaAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    list_filter=('nombre',)
    ordering=('nombre',)
    search_fields=('nombre',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }
    
class DomicilioSearchAdmin(admin.ModelAdmin):
    list_display=('barrio','direccion', 'numero_direccion','depto','piso','localidad','codigo_postal')
    list_filter=('direccion', 'numero_direccion','piso','depto','codigo_postal','localidad','barrio')
    ordering=('barrio',)
    search_fields=('localidad','barrio','direccion')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }

class ClienteAdmin(admin.ModelAdmin):
    list_display=('apellido', 'nombre', 'sexo', 'email', 'telefono_particular')
    list_filter=('nombre', 'apellido', 'sexo', 'email', 'telefono_particular')
    ordering=('apellido',)
    search_fields=('nombre','apellido')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }

class EstadoPedidoAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'descripcion')
    list_display = ('nombre', 'descripcion')
    list_filter = ('nombre', )
    ordering=('nombre',)
    fields =('nombre','descripcion') 
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }  

class DetallePedidoInline(admin.StackedInline, SortableInline):
    model = DetallePedido
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},                 
    }
    
class PedidoAdmin(admin.ModelAdmin):
    search_fields = ('cliente','fechaPedido','estado','servicio', 'tipologia_vivienda')
    list_display = ('cliente', 'fechaPedido', 'hora_entrega', 'servicio', 'tipologia_vivienda', 'precio_envio', 'estado')
    list_filter = ('cliente', 'fechaPedido', 'hora_entrega', 'estado', 'servicio', 'tipologia_vivienda', 'precio_envio')
    ordering=('cliente','fechaPedido','estado')
    
    inlines = [DetallePedidoInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }  
 

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(TipologiaVivienda, TipologiaViviendaAdmin)
admin.site.register(DomicilioSearch, DomicilioSearchAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(EstadoPedido, EstadoPedidoAdmin)
admin.site.register(Pedido, PedidoAdmin)
