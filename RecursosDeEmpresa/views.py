#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from RecursosDeEmpresa.models import Empleado,TipoDocumento
from RecursosDeEmpresa.forms import EmpleadoForm, addEmpleadoForm
# Paginacion en Django
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q 
from django.http import HttpResponseRedirect

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
                lista_empleado = Empleado.objects.filter(Q(nombre__contains=buscar)| Q(legajo__contains=buscar) | Q(apellido__contains=buscar) | Q(numero_documento__contains=buscar))
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

def add_empleado_view(request):
    info = "iniciado"
    if request.method == "POST":
        form = addEmpleadoForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.status = True
            add.save() # Guardamos la informacion                  
            info = "Guardado satisfactoriamente"
            return HttpResponseRedirect('/recursosDeEmpresa/empleados/page/1/')
    else:
        form = addEmpleadoForm()
    ctx = {'form':form,'informacion':info}
    return render_to_response('RecursosDeEmpresa/addEmpleado.html',ctx,context_instance=RequestContext(request)) 

def edit_empleado_view(request,id_emp):
    info = "iniciado"
    emp = Empleado.objects.get(pk=id_emp)
    if request.method == "POST":
        form = addEmpleadoForm(request.POST,request.FILES,instance=emp)
        if form.is_valid():
            edit_prod = form.save(commit=False)            
            edit_prod.status = True
            edit_prod.save() # Guardamos el objeto
            info = "Correcto"
            return HttpResponseRedirect('/recursosDeEmpresa/empleados/page/1/')
    else:
        form = addEmpleadoForm(instance=emp)
    ctx = {'form':form,'informacion':info}
    return render_to_response('RecursosDeEmpresa/editEmpleado.html',ctx,context_instance=RequestContext(request)) 

def singleEmpleado_view(request,id_emp):
    emp = Empleado.objects.get(pk=id_emp)    
    ctx = {'empleado':emp}
    return render_to_response('RecursosDeEmpresa/singleEmpleado.html',ctx,context_instance=RequestContext(request))
