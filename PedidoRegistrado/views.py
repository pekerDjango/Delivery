# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404  
from django.template import RequestContext
from PedidoRegistrado.forms import DomicilioSearchForm, PagoForm, HoraPedidoForm
from django.http import HttpResponseRedirect
from PedidoRegistrado.models import DomicilioSearch, Pedido, DetallePedido, Cliente, Servicio, TipologiaVivienda, EstadoPedido
from ComponentesDePedido.models import Producto, DetalleVersiones, TipoProducto, Menu, Promocion
from RecursosDeEmpresa.models import Sucursal
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from django.contrib.auth.decorators import login_required

def pedidoInformacion_view(request):
    if request.method == "POST":
        form = DomicilioSearchForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.status = True
            add.save() # Guardamos la informacion           
            request.session ["domicilio"] = add
            request.session["pedido"] = None
            request.session["detalles"]={}   
            return HttpResponseRedirect('/pedido/armaTuPedido/')
    else:
        form = DomicilioSearchForm() 
    servicio = Servicio.objects.all()
    tipologia = TipologiaVivienda.objects.all()   
    ctx = {'form': form, 'servicios':servicio, 'tipologias' : tipologia}
    return render_to_response('PedidoRegistrado/pedidoInformacion.html',ctx, context_instance=RequestContext(request))

def actualizarPedidoInformacion_view(request, id_dom): 
    instance = get_object_or_404(DomicilioSearch, id=id_dom)
    form = DomicilioSearchForm(request.POST or None, instance=instance)
    if form.is_valid():
        add = form.save(commit=False)
        add.status = True
        add.save() # Guardamos la informacion           
        request.session ["domicilio"] = add
        return HttpResponseRedirect('/pedido/armaTuPedido/')        
    servicio = Servicio.objects.all()
    tipologia = TipologiaVivienda.objects.all()   
    ctx = {'form': form, 'servicios':servicio, 'tipologias' : tipologia}
    return render_to_response('PedidoRegistrado/pedidoInformacion.html',ctx, context_instance=RequestContext(request))

def armaTuPedido_view(request): 
    tipoProducto = TipoProducto.objects.all()    
    ctx = { 'tipoProducto': tipoProducto}   
    return render_to_response('PedidoRegistrado/armaPedido.html',ctx, context_instance=RequestContext(request))

def productosSolicitados_view(request, codigo):    
    t= TipoProducto.objects.get(codigo=codigo) 
    productos = Producto.objects.filter(tipoProducto=t.codigo)
    ped = request.session["pedido"]        
    ctx = {'productos':productos, 'pedido':ped}   
    return render_to_response('PedidoRegistrado/productosSolicitados.html',ctx, context_instance=RequestContext(request))

def menuDisponibles_view(request):       
    menus = Menu.objects.all()
    ped = request.session["pedido"] 
    ctx = {'productos':menus, 'pedido':ped}   
    return render_to_response('PedidoRegistrado/menuDisponibles.html',ctx, context_instance=RequestContext(request))

def promocionDisponibles_view(request):      
    promos = Promocion.objects.all()
    ped = request.session["pedido"] 
    ctx = { 'productos':promos, 'pedido':ped}   
    return render_to_response('PedidoRegistrado/promosDisponibles.html',ctx, context_instance=RequestContext(request))

def productosPopulares_view(request):       
    productos = Producto.objects.all()
    ped = request.session["pedido"]    
    ctx = { 'productos':productos, 'pedido':ped}  
    return render_to_response('PedidoRegistrado/productosSolicitados.html',ctx, context_instance=RequestContext(request))

def agregarPedido_view(request,cantidad,id_pro,id_tip):  
    fechaPed = datetime.now()
    cli=Cliente.objects.get(pk=1)
    est=EstadoPedido.objects.get(pk=1)
    ser=Servicio.objects.get(pk=1)
    tip=TipologiaVivienda.objects.get(pk=1) 
    pedi = request.session["pedido"] 
    if  pedi is None: 
        p = Pedido(cliente=cli,fechaPedido=fechaPed,estado=est,servicio=ser,tipologia_vivienda=tip,precio_envio=34)
        p.save()
        request.session["pedido"]=p
    ped = request.session["pedido"]      
    productos = []
    htp='index.html'
    if int(id_tip) == 1:
        pro = DetalleVersiones.objects.get(pk=id_pro)   
        precion = pro.precio 
        d = DetallePedido(pedido=ped,cantidad=cantidad,producto=pro,precio=precion)
        d.save()
        productos= Producto.objects.all()
        htp= 'PedidoRegistrado/productosSolicitados.html'
    elif int(id_tip) == 2:
        pro= Menu.objects.get(pk=id_pro)
        precion = pro.precioVenta
        d = DetallePedido(pedido=ped,cantidad=cantidad,menu=pro,precio=precion)
        d.save()
        productos = Menu.objects.all()
        htp= 'PedidoRegistrado/menuDisponibles.html'
    elif int(id_tip) == 3:
        pro= Promocion.objects.get(pk=id_pro)
        precion = pro.precio
        d = DetallePedido(pedido=ped,cantidad=cantidad,promocion=pro,precio=precion)
        d.save()
        productos = Promocion.objects.all()
        htp= 'PedidoRegistrado/promosDisponibles.html'
    ctx = {'productos':productos, 'pedido':ped}
    return render_to_response(htp,ctx,context_instance=RequestContext(request))   
#        ctx = {'menus':menus, 'pedido':ped}
#        return render_to_response('PedidoRegistrado/menuDisponibles.html',ctx,context_instance=RequestContext(request))    
#    lista = request.session["detalles"]
#    lista.append(d)
#    request.session["detalles"] = lista
#    dic = request.session["detalles"]
#    keys = dic.keys()
#    if not pro.id in keys:       
#        dic[pro.id] = [cantidad,pro]
#    else:
#        valor = int (dic[pro.id][0]) + int(cantidad)
#        dic[pro.id] = [valor,pro ]
#    print dic
#    request.session['detalles'] = dic
#    deta = request.session['detalles']            

def eliminarDetalle_view(request,id_det):
    ped = request.session["pedido"]
    d = DetallePedido.objects.get(pk=id_det)
    if d.pedido == ped:
        d.delete()
    productos = Producto.objects.all()
    ctx = {'productos':productos, 'pedido':ped}   
    return render_to_response('PedidoRegistrado/productosSolicitados.html',ctx, context_instance=RequestContext(request))

def detallePedido_view(request):       
    ped = request.session["pedido"]
#    ped.save()
#    for d in ped.getDetallePedido():
#        d.pedido = ped.id
#        d.save()                
    ctx = { 'pedido':ped}  
    return render_to_response('PedidoRegistrado/detallePedido.html',ctx, context_instance=RequestContext(request))

@login_required(login_url='/login')
def detallePago_view(request):
    horaPedido = datetime.now().time()  
    ped = request.session["pedido"]
    total = ped.precio_envio
    vuelto=0
    for d in ped.getDetallePedido():
        total += float(d.precio) * float(d.cantidad)    
    if request.method == "POST":
        form = PagoForm(request.POST,request.FILES, precioTotal = total)
        form2 = HoraPedidoForm(request.POST,request.FILES)         
        if form.is_valid():
            importe= form.cleaned_data['importePagar']           
            vuelto = float(0 if importe is None else importe) - total                   
            request.session["importe"] = (importe,vuelto)
        elif form2.is_valid():
            horaPedido = form2.cleaned_data['horaPedir']
            request.session["horaPedir"] = horaPedido
            return HttpResponseRedirect('/pedido/armaTuPedido/detallePedido/detallePago/pedidoFinalizado/')  
    else:
        form = PagoForm(precioTotal = total)
        form2 = HoraPedidoForm()          
    ped = request.session["pedido"]
    horaActual = datetime.now().time()       
    ctx = { 'pedido':ped, 'form':form,'form2':form2, 'vuelto':vuelto, 'horaActual':horaActual}  
    return render_to_response('PedidoRegistrado/detallePago.html',ctx, context_instance=RequestContext(request))

def pedidoFinalizado_view(request):
    ped = request.session["pedido"]
    total = 0    
    for d in ped.getDetallePedido():
        if not d.producto is None:
            total += int(d.producto.producto.tiempoPreparacion) * d.cantidad
        elif not d.menu is None:            
            total += d.menu.tiempoPreparacionTotal() * d.cantidad 
        elif not d.promocion is None:
            total += d.promocion.tiempoPreparacionTotal() * d.cantidad      
    tupla = request.session["importe"]
    importe = tupla[0]
    vuelto = tupla[1]
    horaPedir =  request.session["horaPedir"]  
    dt = datetime.combine(date.today(), horaPedir) + timedelta(minutes=total)
    ped.hora_entrega = dt.time()
    ped.save()
    ctx = { 'pedido':ped, 'importe':importe, 'vuelto': vuelto, 'horaPedir':horaPedir,'total':total}  
    return render_to_response('PedidoRegistrado/pedidoFinalizado.html',ctx, context_instance=RequestContext(request))

def cerrarPedido_view(request):
    request.session ["domicilio"] = None
    request.session["pedido"] = None 
    return render_to_response('index.html', context_instance=RequestContext(request))


     
    