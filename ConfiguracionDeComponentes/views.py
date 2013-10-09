#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from ConfiguracionDeComponentes.forms import LoginForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

def index_view(request):     
    return render_to_response('index.html', context_instance=RequestContext(request))

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect(next)
                else:
                    mensaje = "usuario y/o password incorrecto"
        next = request.REQUEST.get("next")
        print next
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje,'next':next}
        return render_to_response('ConfiguracionDeComponentes/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


