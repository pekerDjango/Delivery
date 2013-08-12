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

admin.site.register(TipoIngrediente)
admin.site.register(Clasificacion)
admin.site.register(UnidadDeMedida)
admin.site.register(TipoProducto)
admin.site.register(Ingrediente)
admin.site.register(DetalleIngredientes)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Menu)
admin.site.register(Frecuencia)
admin.site.register(Programacion)
admin.site.register(Promocion)
admin.site.register(DetallePromocion)
admin.site.register(Version)
