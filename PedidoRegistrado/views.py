# Create your views here.
from PedidoRegistrado.models import Servicio
from django.shortcuts import render_to_response 
from django.template import RequestContext

def pedidoInformacion_view(request):
    servicio = Servicio.objects.all()
    ctx = {'servicios':servicio}
    return render_to_response('PedidoRegistrado/pedidoInformacion.html',ctx, context_instance=RequestContext(request))