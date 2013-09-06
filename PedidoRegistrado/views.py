# Create your views here.
from PedidoRegistrado.models import Servicio, TipologiaVivienda
from django.shortcuts import render_to_response 
from django.template import RequestContext
from PedidoRegistrado.forms import DomicilioSearchForm
from django.http import HttpResponseRedirect
from PedidoRegistrado.models import DomicilioSearch
from ComponentesDePedido.models import Producto, DetalleVersiones

def pedidoInformacion_view(request):
    if request.method == "POST":
        form = DomicilioSearchForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.status = True
            add.save() # Guardamos la informacion
            request.session['domicilio'] = add.id
            return HttpResponseRedirect('/pedido/armaTuPedido/')
    else:
        form = DomicilioSearchForm() 
    servicio = Servicio.objects.all()
    tipologia = TipologiaVivienda.objects.all()
    ctx = {'form': form, 'servicios':servicio, 'tipologias' : tipologia}
    return render_to_response('PedidoRegistrado/pedidoInformacion.html',ctx, context_instance=RequestContext(request))

def armaTuPedido_view(request):
    dom =   request.session['domicilio']
    domicilio = DomicilioSearch.objects.get(id=dom)
    productos = Producto.objects.all()
    detalleProducto = DetalleVersiones.objects.all()
    print domicilio
    ctx = {'domicilio':domicilio, 'productos':productos, 'detalleProducto':detalleProducto}   
    return render_to_response('PedidoRegistrado/armaPedido.html',ctx, context_instance=RequestContext(request))