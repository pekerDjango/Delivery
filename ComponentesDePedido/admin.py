#encoding:utf-8
from ComponentesDePedido.models import TipoIngrediente
from ComponentesDePedido.models import Clasificacion
from ComponentesDePedido.models import UnidadDeMedida
from ComponentesDePedido.models import TipoProducto
from ComponentesDePedido.models import Version
from ComponentesDePedido.models import Ingrediente
from ComponentesDePedido.models import DetalleIngredientes
from ComponentesDePedido.models import Producto
from ComponentesDePedido.models import DetalleVersiones
from ComponentesDePedido.models import Menu
from ComponentesDePedido.models import Frecuencia
from ComponentesDePedido.models import Programacion
from ComponentesDePedido.models import Promocion
from ComponentesDePedido.models import DetallePromocionProducto
from ComponentesDePedido.models import DetallePromocionMenu
from ComponentesDePedido.models import DetalleMenu
from ComponentesDePedido.models import DiaSemana
from django.contrib import admin
from django.forms import ModelForm
from django_admin_bootstrapped.admin.models import SortableInline
from django.forms import TextInput, Textarea, SelectMultiple
from django.db import models
from django.contrib.admin.widgets import AdminFileWidget
from form_utils.widgets import ImageWidget


class DetalleVersionInline(admin.StackedInline, SortableInline):
    model = DetalleVersiones
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget}          
    }  
    
class DetalleIngredientesInline(admin.StackedInline, SortableInline):
    model = DetalleIngredientes
    verbose_name_plural = "Detalle de Ingredientes"
    extra = 1    

class ProductoAdmin(admin.ModelAdmin):
    inlines = [DetalleVersionInline, DetalleIngredientesInline]
    search_fields = ('codigo', 'nombre', 'tipoProducto__nombre')
    list_display = ('codigo', 'nombre' , 'tipoProducto', 'estado')
    list_filter = ('codigo', 'nombre', 'tipoProducto')
    ordering=('codigo','nombre',)
    fields =('codigo','nombre', 'tiempoPreparacion', 'tipoProducto', 'version','estado')
    readonly_fields =('codigo',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},      
    }   
    
class TipoIngredienteAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')
    ordering=('codigo','nombre',)
    fields =('codigo','nombre')
    readonly_fields =('codigo',)   

class UnidadDeMedidaAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')
    ordering=('codigo','nombre',)
    fields =('codigo','nombre')
    readonly_fields =('codigo',)

class TipoProductoAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre','Vista_Previa')
    list_filter = ('codigo', 'nombre')
    ordering=('codigo','nombre',)
    fields =('codigo','nombre','imagen')
    readonly_fields =('codigo',)

class ClasificacionAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'descripcion')
    list_display = ('nombre', 'descripcion')
    list_filter = ('nombre', 'descripcion')
    ordering=('nombre',)
    
class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre' )
    list_display = ('codigo', 'nombre', 'unidadDeMedida', 'precio', 'stockActual', 'stockMinimo')
    list_filter = ('codigo', 'nombre', 'unidadDeMedida', 'precio', 'stockActual', 'stockMinimo') 
    fields =('codigo','nombre','tipoIngrediente','unidadDeMedida','imagen','stockActual','stockMinimo','stockCorte','precio')
    readonly_fields =('codigo',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    } 

class VersionAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')
    ordering=('codigo','nombre',)
    fields =('codigo','nombre','clasificacion')
    readonly_fields =('codigo',)

class DetalleMenuInline(admin.StackedInline, SortableInline):
    model = DetalleMenu
    extra = 1
    
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre', 'precioVenta','Vista_Previa')
    list_filter = ('codigo', 'nombre','precioVenta')
    ordering=('codigo','nombre',)
    fields =('codigo','nombre','precioVenta','imagen')
    readonly_fields =('codigo',)
    inlines = [DetalleMenuInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    }    
    
class DetallePromocionProductoInline(admin.StackedInline, SortableInline):
    model = DetallePromocionProducto
    extra = 1
    
class DetallePromocionMenuInline(admin.StackedInline, SortableInline):
    model = DetallePromocionMenu
    extra = 1

class ProgramacionInline(admin.StackedInline, SortableInline):
    model = Programacion
    extra = 1
    max_num = 1
#    filter_horizontal = ("diaSemana",)
    formfield_overrides = {
                           models.ManyToManyField: {'widget': SelectMultiple(attrs={'width':'100'})}
                           }    

class PromocionAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre', 'precio', 'stock','Vista_Previa', 'estado')
    list_filter = ('codigo', 'nombre')
    ordering=('codigo','nombre',)
    fields =('codigo','nombre','descripcion','imagen', 'precio', 'stock', 'tiempoPreparacion')
    readonly_fields =('codigo',)
    inlines = [ProgramacionInline, DetallePromocionProductoInline, DetallePromocionMenuInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    } 
    
class ProgramacionAdmin(admin.ModelAdmin):
    fields =( 'diaSemana','fechaDesde','fechaHasta','horaDesde','horaHasta')
    
class DetalleVersionesAdmin(admin.ModelAdmin):   
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})}, 
        models.DecimalField: {'widget': TextInput(attrs={'size':'20'})},      
    }  
    
admin.site.register(TipoIngrediente, TipoIngredienteAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(UnidadDeMedida, UnidadDeMedidaAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
#admin.site.register(DetalleIngredientes)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Frecuencia)
#admin.site.register(Programacion,ProgramacionAdmin)
admin.site.register(Promocion, PromocionAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(DiaSemana)
#admin.site.register(DetalleVersiones, DetalleVersionesAdmin)