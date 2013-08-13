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
from ComponentesDePedido.models import DetallePromocion
from django.contrib import admin
from django_admin_bootstrapped.admin.models import SortableInline

admin.site.register(DetalleVersiones)

class DetalleVersionInLine(admin.StackedInline, SortableInline):
    model = DetalleVersiones
    extra = 1
    
class DetalleIngredientesInLine(admin.StackedInline, SortableInline):
    model = DetalleIngredientes
    verbose_name_plural = "Detalle de Ingredientes"
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = [DetalleVersionInLine, DetalleIngredientesInLine]
    search_fields = ('codigo', 'nombre', 'tipoProducto')
    list_display = ('codigo', 'nombre' , 'tipoProducto', )
    list_filter = ('codigo', 'nombre', 'tipoProducto')
    
class TipoIngredienteAdmin(admin.ModelAdmin):
    search_fields = ('codigoTipoIngrediente', 'nombreTipoIngrediente')
    list_display = ('codigoTipoIngrediente', 'nombreTipoIngrediente')
    list_filter = ('codigoTipoIngrediente', 'nombreTipoIngrediente')

class UnidadDeMedidaAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')

class TipoProductoAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')

class ClasificacionAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'descripcion')
    list_display = ('nombre', 'descripcion')
    list_filter = ('nombre', 'descripcion')
    
class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre' )
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre', 'unidadDeMedida', 'precio', 'stockActual', 'stockMinimo')

class MenuAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre', 'precioVenta')
    list_filter = ('codigo', 'nombre')
    
class PromocionAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre', 'precio', 'stock')
    list_filter = ('codigo', 'nombre')

class VersionAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'nombre')
    list_display = ('codigo', 'nombre')
    list_filter = ('codigo', 'nombre')

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
admin.site.register(DetallePromocion)
admin.site.register(Version, VersionAdmin)
