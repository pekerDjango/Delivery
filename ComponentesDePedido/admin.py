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

admin.site.register(DetalleVersiones)

class DetalleVersionInline(admin.StackedInline, SortableInline):
    model = DetalleVersiones
    extra = 1
class DetalleIngredientesInline(admin.StackedInline, SortableInline):
    model = DetalleIngredientes
    verbose_name_plural = "Detalle de Ingredientes"
    extra = 1
    


class ProductoAdmin(admin.ModelAdmin):
    inlines = [DetalleVersionInline, DetalleIngredientesInline]
    search_fields = ('codigo', 'nombre', 'tipoProducto__nombre')
    list_display = ('codigo', 'nombre' , 'tipoProducto', )
    list_filter = ('codigo', 'nombre', 'tipoProducto')
    fields =('codigo','nombre', 'tiempoPreparacion', 'tipoProducto', 'version','unidadDeMedida')
    readonly_fields =('codigo',)   
    
class TipoIngredienteAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')
    fields =('codigo','nombre')
    readonly_fields =('codigo',)   

class UnidadDeMedidaAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')
    fields =('codigo','nombre')
    readonly_fields =('codigo',)

class TipoProductoAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')
    fields =('codigo','nombre')
    readonly_fields =('codigo',)

class ClasificacionAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'descripcion')
    list_display = ('nombre', 'descripcion')
    list_filter = ('nombre', 'descripcion')
    
class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre' )
    list_display = ('codigo', 'nombre', 'unidadDeMedida', 'precio', 'stockActual', 'stockMinimo')
    list_filter = ('codigo', 'nombre', 'unidadDeMedida', 'precio', 'stockActual', 'stockMinimo') 
    fields =('codigo','nombre','tipoIngrediente','unidadDeMedida','stockActual','stockMinimo','precio')
    readonly_fields =('codigo',)   

class VersionAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')
    fields =('codigo','nombre')
    readonly_fields =('codigo',)

class DetalleMenuInline(admin.StackedInline, SortableInline):
    model = DetalleMenu
    extra = 1
    
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre', 'precioVenta','Vista_Previa')
    list_filter = ('codigo', 'nombre','precioVenta')
    fields =('codigo','nombre','precioVenta','imagen')
    readonly_fields =('codigo',)
    inlines = [DetalleMenuInline]
    
    
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

class PromocionAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre', 'precio', 'stock','Vista_Previa')
    list_filter = ('codigo', 'nombre')
    fields =('codigo','nombre','imagen', 'precio', 'stock', 'tiempoPreparacion')
    readonly_fields =('codigo',)
    inlines = [ProgramacionInline, DetallePromocionProductoInline, DetallePromocionMenuInline]
    
class ProgramacionAdmin(admin.ModelAdmin):
    fields =( 'diaSemana','fechaDesde','fechaHasta','horaDesde','horaHasta')
    
admin.site.register(TipoIngrediente, TipoIngredienteAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(UnidadDeMedida, UnidadDeMedidaAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(DetalleIngredientes)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Frecuencia)
admin.site.register(Programacion)
admin.site.register(Promocion, PromocionAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(DiaSemana)
