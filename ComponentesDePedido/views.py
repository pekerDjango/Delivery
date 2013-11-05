# Create your views here.

from ComponentesDePedido.models import Producto, DetalleVersiones, TipoProducto
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


def productoListado_view(request):
	lista_productos = Producto.objects.all()
	print lista_productos
	nro=1
	lista=[]
	for producto in lista_productos:
    		tipo_producto_imagen= TipoProducto.objects.get(producto=nro).imagen
    		
    		tipo_producto_nombre= TipoProducto.objects.get(producto=nro).nombre
    		
    		print tipo_producto_nombre
    		print tipo_producto_imagen
    		print nro
    		nro= nro + 1

    		
    		
    		
	ctx={'tipo_producto_imagen':tipo_producto_imagen,'tipo_producto_nombre':tipo_producto_nombre,'lista_productos':lista_productos}
 	return render_to_response('ComponentesDePedido/ListadoProductos.html',ctx,context_instance=RequestContext(request))
		
    	
    	
   		
    
   	   
