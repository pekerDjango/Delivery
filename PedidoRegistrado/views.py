# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404  
from django.template import RequestContext
from PedidoRegistrado.forms import DomicilioSearchForm, PagoForm, HoraPedidoForm
from django.http import HttpResponseRedirect
from PedidoRegistrado.models import DomicilioSearch, Pedido, DetallePedido, Cliente, Servicio, TipologiaVivienda, EstadoPedido, ProductoParaArmar, SeccionProducto, VersionProducto, ProductoArmado, DetalleProductoArmado, IngredientesSeccion
from ComponentesDePedido.models import Producto, DetalleVersiones, TipoProducto, Menu, Promocion
from RecursosDeEmpresa.models import Sucursal
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from SiGeP.settings import URL_LOGIN

def pedidoInformacion_view(request):
    if request.method == "POST":
        form = DomicilioSearchForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.status = True          
            add.save() # Guardamos la informacion           
            request.session ["domicilio"] = add
            request.session["pedido"] = None                       
            request.session["sucursal"] = Sucursal.objects.get(pk=1)
            request.session["detalles"]={}
            Dom= request.session["domicilio"]
            if Dom.servicio.nombre == "Sucursales":
                return HttpResponseRedirect('/pedido/sucursales/')
            else:          
                return HttpResponseRedirect('/pedido/armaTuPedido/')
    else:
        form = DomicilioSearchForm()
        request.session ["domicilio"] = None 
        request.session["sucursal"] = None 
    servicio = Servicio.objects.all()
    tipologia = TipologiaVivienda.objects.all()
    boton = 'Iniciar Pedido'   
    ctx = {'form': form, 'servicios':servicio, 'tipologias' : tipologia,'boton':boton}
    return render_to_response('PedidoRegistrado/pedidoInformacion.html',ctx, context_instance=RequestContext(request))

def actualizarPedidoInformacion_view(request, id_dom): 
    instance = get_object_or_404(DomicilioSearch, id=id_dom)
    form = DomicilioSearchForm(request.POST or None, instance=instance)
    if form.is_valid():
        add = form.save(commit=False)
        add.status = True
        add.save() # Guardamos la informacion           
        request.session ["domicilio"] = add
        Dom= request.session["domicilio"]
        if Dom.servicio.nombre == "Sucursales":
            return HttpResponseRedirect('/pedido/sucursales/')
        else:          
            return HttpResponseRedirect('/pedido/armaTuPedido/')        
    servicio = Servicio.objects.all()
    tipologia = TipologiaVivienda.objects.all()   
    boton = 'Continuar'   
    ctx = {'form': form, 'servicios':servicio, 'tipologias' : tipologia,'boton':boton}
    return render_to_response('PedidoRegistrado/pedidoInformacion.html',ctx, context_instance=RequestContext(request))

def armaTuPedido_view(request): 
    tipoProducto = TipoProducto.objects.all()
    producto = ProductoParaArmar.objects.all()
    request.session["productoArmado"]= None    
    ctx = { 'tipoProducto': tipoProducto, 'productoParaArmar': producto}   
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
        p = Pedido(cliente=cli,fechaPedido=fechaPed,estado=est,servicio=ser,tipologia_vivienda=tip,precio_envio=8)
        p.save()
        request.session["pedido"]=p
    ped = request.session["pedido"]  
    if int(id_tip) == 1:
        pro = DetalleVersiones.objects.get(pk=id_pro)   
        precion = pro.precio 
        d = DetallePedido(pedido=ped,cantidad=cantidad,producto=pro,precio=precion)
        d.save()        
        tipo = pro.producto.tipoProducto.codigo
        return HttpResponseRedirect('/pedido/armaTuPedido/productosSolicitados/'+str(tipo))
    elif int(id_tip) == 2:
        pro= Menu.objects.get(pk=id_pro)
        precion = pro.precioVenta
        d = DetallePedido(pedido=ped,cantidad=cantidad,menu=pro,precio=precion)
        d.save()
        return HttpResponseRedirect('/pedido/armaTuPedido/menusDisponibles/')
    elif int(id_tip) == 3:
        pro= Promocion.objects.get(pk=id_pro)
        precion = pro.precio
        d = DetallePedido(pedido=ped,cantidad=cantidad,promocion=pro,precio=precion)
        d.save()
        return HttpResponseRedirect('/pedido/armaTuPedido/promosDisponibles/')           

def actualizar_detalle_pedido_view(request,nueva_cantidad,id_det):
    pedi = request.session["pedido"] 
    if pedi is not None:
        DetallePedido.objects.filter(pk = id_det).update(cantidad = nueva_cantidad)
    #productos= Producto.objects.all()
    
    ctx = {'pedido':pedi}   
    return render_to_response('PedidoRegistrado/detallesDePedido.html',ctx, context_instance=RequestContext(request))
    
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
    ctx = { 'pedido':ped}   
#    return render_to_response('PedidoRegistrado/productosSolicitados.html',ctx, context_instance=RequestContext(request))
    return render_to_response('PedidoRegistrado/detallesDePedido.html',ctx, context_instance=RequestContext(request))

def detallePedido_view(request):       
    ped = request.session["pedido"]
#    ped.save()
#    for d in ped.getDetallePedido():
#        d.pedido = ped.id
#        d.save()                
    ctx = { 'pedido':ped}  
    return render_to_response('PedidoRegistrado/detallePedido.html',ctx, context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def detallePago_view(request):
    request.session.set_expiry(900)
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
    request.session["sucursal"] = None
    return render_to_response('index.html', context_instance=RequestContext(request))

def productoParaArmar_view(request,id_pro):
    fechaPed = datetime.now()
    cli=Cliente.objects.get(pk=1)
    est=EstadoPedido.objects.get(pk=1)
    ser=Servicio.objects.get(pk=1)
    tip=TipologiaVivienda.objects.get(pk=1) 
    pedi = request.session["pedido"] 
    if  pedi is None: 
        p = Pedido(cliente=cli,fechaPedido=fechaPed,estado=est,servicio=ser,tipologia_vivienda=tip,precio_envio=8)
        p.save()
        request.session["pedido"]=p
    ped = request.session["pedido"]
    pro = ProductoParaArmar.objects.get(pk=id_pro)    
    request.session["productoArmar"]= pro    
    request.session["exclusion"]= {}
    detalleVersiones = pro.getDetalleVersiones()
    secciones = SeccionProducto.objects.filter(producto=pro).order_by('orden')
    productoArmado = request.session["productoArmado"]         
    ctx = { 'pedido':ped, 'detalleVersiones': detalleVersiones, 'secciones': secciones, 'productoArmar': pro, 'productoArmado':productoArmado}  
    return render_to_response('PedidoRegistrado/productoParaArmar.html',ctx ,context_instance=RequestContext(request))

def sucursales_view(request):
    lista_sucursal=Sucursal.objects.all()
    return render_to_response('PedidoRegistrado/sucursales.html',{'lista_sucursal':lista_sucursal},context_instance=RequestContext(request))

def sucursalElegir_view(request, id_suc):
    Dom= request.session["domicilio"]
    request.session["sucursal"] = Sucursal.objects.get(pk=id_suc) 
    instance = get_object_or_404(DomicilioSearch, id=Dom.id)
    form = DomicilioSearchForm(request.POST or None, instance=instance)
    if form.is_valid():
        add = form.save(commit=False)
        add.status = True
        add.save() # Guardamos la informacion           
        request.session ["domicilio"] = add
        return HttpResponseRedirect('/pedido/armaTuPedido/')        
    servicio = Servicio.objects.all()
    tipologia = TipologiaVivienda.objects.all()   
    boton = 'Continuar'   
    ctx = {'form': form, 'servicios':servicio, 'tipologias' : tipologia,'boton':boton}
    return render_to_response('PedidoRegistrado/pedidoInformacion.html',ctx, context_instance=RequestContext(request))

def productoArmado_view(request,id_ver):
    ped = request.session["pedido"]
    pro = request.session["productoArmado"]
    if pro is None:
        proArm = request.session["productoArmar"]    
        ver = VersionProducto.objects.get(pk=id_ver) 
        productoArmado = ProductoArmado(producto=proArm, version=ver)
        productoArmado.save()
        request.session["productoArmado"]= productoArmado
    else:
        ver = VersionProducto.objects.get(pk=id_ver)
        productoArmado = ProductoArmado.objects.get(pk=pro.id)
        productoArmado.version = ver
        productoArmado.save()
        request.session["productoArmado"]= productoArmado      
    pro = request.session["productoArmado"]
    ctx = { 'pedido':ped, 'productoArmado': pro}  
    return render_to_response('PedidoRegistrado/detallesDePedido.html',ctx, context_instance=RequestContext(request))

def productoArmadoIngrediente_view(request,id_ing):    
    productoArmado =  request.session["productoArmado"]
    ing = IngredientesSeccion.objects.get(pk=id_ing)
    dic = request.session["exclusion"]
    keys = dic.keys()
    if not ing.seccion.orden in keys:
        dic[ing.seccion.orden] = [1,ing.seccion]
        detalle = DetalleProductoArmado(producto=productoArmado, ingrediente= ing)
        detalle.save()
    else:
        if ing.seccion.cantidad_exclusiones  >= (dic[ing.seccion.orden][0]+1):
            dic[ing.seccion.orden] = [dic[ing.seccion.orden][0]+1,ing.seccion]
            detalle = DetalleProductoArmado(producto=productoArmado, ingrediente= ing)
            detalle.save()
    request.session["exclusion"] = dic   
    ped = request.session["pedido"]
    ctx = { 'pedido':ped, 'productoArmado': productoArmado}  
    return render_to_response('PedidoRegistrado/detallesDePedido.html',ctx, context_instance=RequestContext(request))

def tuProducto_view(request):
    productoArmado =  request.session["productoArmado"]
    secciones = SeccionProducto.objects.filter(producto=productoArmado.producto).order_by('orden')  
    ctx = { 'productoArmado': productoArmado, 'secciones': secciones}  
    return render_to_response('PedidoRegistrado/tuProducto.html',ctx, context_instance=RequestContext(request))

def guardarProducto_view(request):
    productoArmado =  request.session["productoArmado"]
    ped = request.session["pedido"]  
    precion = productoArmado.version.precio 
    d = DetallePedido(pedido=ped,cantidad=1,producto_armado=productoArmado,precio=precion)
    d.save()        
    return HttpResponseRedirect('/pedido/armaTuPedido/')


     
    