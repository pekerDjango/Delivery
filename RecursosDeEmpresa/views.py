#encoding:utf-8
from django.shortcuts import render_to_response,  get_object_or_404 
from django.template import RequestContext
from RecursosDeEmpresa.models import Empleado
from RecursosDeEmpresa.models import Sucursal
from RecursosDeEmpresa.forms import EmpleadoForm, addEmpleadoForm, DeleteEmpleadoForm
# Paginacion en Django
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def indexAdmin_view(request):  
    mensaje = "Aquí realice su administración"
    ctx = {'msg':mensaje}
    return render_to_response('indexAdmin.html',ctx,context_instance=RequestContext(request))


@login_required(login_url='/login')
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
            return HttpResponseRedirect('/empleado/%s'%add.id)
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
            edit_emp = form.save(commit=False)            
            edit_emp.status = True
            edit_emp.save() # Guardamos el objeto
            info = "Correcto"
            return HttpResponseRedirect('/empleado/%s/'%edit_emp.legajo)
    else:
        form = addEmpleadoForm(instance=emp)
    ctx = {'form':form,'informacion':info}
    return render_to_response('RecursosDeEmpresa/editEmpleado.html',ctx,context_instance=RequestContext(request)) 

def singleEmpleado_view(request,id_emp):
    emp = Empleado.objects.get(pk=id_emp)    
    ctx = {'empleado':emp}
    return render_to_response('RecursosDeEmpresa/singleEmpleado.html',ctx,context_instance=RequestContext(request))

def delete_empleado_view(request, id_emp):
    new_to_delete = get_object_or_404(Empleado, legajo=id_emp)
    #+some code to check if this object belongs to the logged in user
    if request.method == 'POST':
        form = DeleteEmpleadoForm(request.POST, instance=new_to_delete)
        if form.is_valid(): # checks CSRF
            new_to_delete.delete()
            return HttpResponseRedirect("/recursosDeEmpresa/empleados/page/1/") # wherever to go after deleting
    else:
        form = DeleteEmpleadoForm(instance=new_to_delete)
    ctx = {'form':form, 'empleado':new_to_delete}
    return render_to_response('RecursosDeEmpresa/deleteEmpleado.html',ctx,context_instance=RequestContext(request)) 

def sucursal_view(request):
    lista_sucursal=Sucursal.objects.all()
    return render_to_response('RecursosDeEmpresa/sucursales.html',{'lista_sucursal':lista_sucursal},context_instance=RequestContext(request))


