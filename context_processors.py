from RecursosDeEmpresa.models import Sucursal
from PedidoRegistrado.models import DomicilioSearch

def domicilio_req(request):
    domi = None
    if "domicilio" in request.session:
        domi= request.session["domicilio"]
        return domi
    else:
        domi=DomicilioSearch.objects.get(pk=1)

def my_processor(request):
    context = {"domicilio":domicilio_req(request),
               "sucursal":Sucursal.objects.get(pk=1)                
    }
    return context