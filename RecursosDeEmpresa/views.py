#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from RecursosDeEmpresa.models import TipoDocumento
# Paginacion en Django
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def tipoDocumento_view(request, pagina):
    lista_tipo = TipoDocumento.objects.all() # Select * from ventas_productos where status = True
    paginator = Paginator(lista_tipo,3) # Cuantos productos quieres por pagina? = 3
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        tipos = paginator.page(page)
    except (EmptyPage,InvalidPage):
        tipos = paginator.page(paginator.num_pages)
    ctx = {'tipos':tipos}
    return render_to_response('RecursosDeEmpresa/tipoDocumento.html',ctx,context_instance=RequestContext(request))# Create your views here.

def indexAdmin_view(request):  
    mensaje = "Aquí realice su administración"
    ctx = {'msg':mensaje}
    return render_to_response('indexAdmin.html',ctx,context_instance=RequestContext(request))
