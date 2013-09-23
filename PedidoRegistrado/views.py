# Create your views here.
from django.shortcuts import render_to_response 
from django.template import RequestContext
from PedidoRegistrado.forms import DomicilioSearchForm, ProductoPedidoForm, PagoForm, horaPedidoForm
from django.http import HttpResponseRedirect
from PedidoRegistrado.models import DomicilioSearch, Pedido, DetallePedido, Cliente, Servicio, TipologiaVivienda, EstadoPedido
from ComponentesDePedido.models import Producto, DetalleVersiones, TipoProducto, Menu, Promocion
from RecursosDeEmpresa.models import Sucursal
import datetime
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

def armaTuPedido_view(request): 
    tipoProducto = TipoProducto.objects.all()    
    ctx = { 'tipoProducto': tipoProducto}   
    return render_to_response('PedidoRegistrado/armaPedido.html',ctx, context_instance=RequestContext(request))

def productosSolicitados_view(request, codigo):    
    t= TipoProducto.objects.get(codigo=codigo) 
    productos = Producto.objects.filter(tipoProducto=t.codigo)       
    ctx = {'productos':productos}   
    return render_to_response('PedidoRegistrado/productosSolicitados.html',ctx, context_instance=RequestContext(request))

def menuDisponibles_view(request):       
    menus = Menu.objects.all()
    ctx = {'menus':menus}   
    return render_to_response('PedidoRegistrado/menuDisponibles.html',ctx, context_instance=RequestContext(request))

def promocionDisponibles_view(request):      
    promos = Promocion.objects.all()
    ctx = { 'promos':promos}   
    return render_to_response('PedidoRegistrado/promosDisponibles.html',ctx, context_instance=RequestContext(request))

def productosPopulares_view(request):       
    productos = Producto.objects.all()
    form = ProductoPedidoForm()    
    ctx = { 'productos':productos, 'form': form}  
    return render_to_response('PedidoRegistrado/productosSolicitados.html',ctx, context_instance=RequestContext(request))

def agregarPedido_view(request,cantidad,id_pro):  
    fechaPed = datetime.datetime.now()
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
    pro= DetalleVersiones.objects.get(pk=id_pro)  
    cant=cantidad
    precion = pro.precio
    d = DetallePedido(pedido=ped,cantidad=cant,producto=pro,precio=precion)
#    d = DetallePedido(cantidad=cant,producto=pro,precio=precion)
    d.save()
#    lista = request.session["detalles"]
#    lista.append(d)
#    request.session["detalles"] = lista
    dic = request.session["detalles"]
    keys = dic.keys()
    if not pro.id in keys:       
        dic[pro.id] = [cantidad,pro]
    else:
        valor = int (dic[pro.id][0]) + int(cantidad)
        dic[pro.id] = [valor,pro ]
    print dic
    request.session['detalles'] = dic
    deta = request.session['detalles']            
    productos= Producto.objects.all()   
    ctx = {'productos':productos, 'pedido':ped,'detalles':deta}
    return render_to_response('PedidoRegistrado/productosSolicitados.html',ctx,context_instance=RequestContext(request))

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
    ped = request.session["pedido"]
    total = ped.precio_envio
    vuelto=0
    for d in ped.getDetallePedido():
        total += float(d.precio) * float(d.cantidad)    
    if request.method == "POST":
        form = PagoForm(request.POST, precioTotal = total)        
        if form.is_valid():
            importe= form.cleaned_data['importePagar']
            importeFloat = float(importe)
#            vuelto = importeFloat - total            
            vuelto = float(0 if importe is None else importe) - total          
#            request.session ["vuelto"]=vuelto            
    else:
        form = PagoForm(precioTotal = total)
        form2 = horaPedidoForm()        
    
    ped = request.session["pedido"]      
    ctx = { 'pedido':ped, 'form':form, 'vuelto':vuelto}  
    return render_to_response('PedidoRegistrado/detallePago.html',ctx, context_instance=RequestContext(request))

def pedidoFinalizado_view(request):
    ped = request.session["pedido"]
    horaActual = datetime.datetime.now().time()         
    ctx = { 'pedido':ped, 'horaActual':horaActual}  
    return render_to_response('PedidoRegistrado/pedidoFinalizado.html',ctx, context_instance=RequestContext(request))

def cerrarPedido_view(request):
    request.session ["domicilio"] = None
    request.session["pedido"] = None 
    return render_to_response('index.html', context_instance=RequestContext(request))


     
    