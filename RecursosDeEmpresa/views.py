#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from RecursosDeEmpresa.models import Empleado,TipoDocumento
from RecursosDeEmpresa.forms import EmpleadoForm
# Paginacion en Django
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q

def tipoDocumento_view(request, pagina):
    lista_tipo = TipoDocumento.objects.all() 
    paginator = Paginator(lista_tipo,3) 
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        tipos = paginator.page(page)
    except (EmptyPage,InvalidPage):
        tipos = paginator.page(paginator.num_pages)
    ctx = {'tipos':tipos}
    return render_to_response('RecursosDeEmpresa/tipoDocumento.html',ctx,context_instance=RequestContext(request))

def indexAdmin_view(request):  
    mensaje = "Aquí realice su administración"
    ctx = {'msg':mensaje}
    return render_to_response('indexAdmin.html',ctx,context_instance=RequestContext(request))

def empleado_view(request, pagina):
    lista_empleado = Empleado.objects.all() 
    if request.method=='POST':
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            buscar = formulario.cleaned_data['Buscar']
            if not buscar=='':
                lista_empleado = Empleado.objects.filter(Q(nombre__contains=buscar)| Q(legajo__contains=buscar) | Q(apellido__contains=buscar))
    else:
        formulario = EmpleadoForm()
    paginator = Paginator(lista_empleado,3) 
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        empleados = paginator.page(page)
    except (EmptyPage,InvalidPage):
        empleados = paginator.page(paginator.num_pages)
    ctx = {'form':formulario,'empleados':empleados}
    return render_to_response('RecursosDeEmpresa/empleados.html',ctx,context_instance=RequestContext(request))


    
