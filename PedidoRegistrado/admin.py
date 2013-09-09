from django.contrib import admin
from PedidoRegistrado.models import Servicio, TipologiaVivienda, DomicilioSearch, Cliente, EstadoPedido, Pedido, EstadoDetallePedido, DetallePedido
from form_utils.widgets import ImageWidget
from django.db import models
from django.forms import TextInput, Textarea
from django_admin_bootstrapped.admin.models import SortableInline

class ServicioAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }
    
class TipologiaViviendaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }
    
class DomicilioSearchAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }

class ClienteAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }

class EstadoPedidoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }
    
class EstadoDetallePedidoAdmin(admin.ModelAdmin):
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
admin.site.register(EstadoDetallePedido, EstadoDetallePedidoAdmin )
admin.site.register(Pedido, PedidoAdmin)
