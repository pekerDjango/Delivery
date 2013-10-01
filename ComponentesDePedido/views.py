# Create your views here.

from ComponentesDePedido.models import Producto, DetalleVersiones, TipoProducto
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def productoListado_view(request):
    lista_productos = Producto.objects.all()
    lista_versiones_productos = DetalleVersiones.objects.all()
    lista_tipos_productos = TipoProducto.objects.all()
    ctx = {'lista_productos':lista_productos, 'lista_versiones': lista_versiones_productos,
            'lista_tipos_productos': lista_tipos_productos}
    return render_to_response('ComponentesDePedido/ListadoProductos.html',ctx,context_instance=RequestContext(request))
    