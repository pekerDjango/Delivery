from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from ConfiguracionDeComponentes.forms import ExRegistrationForm
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SiGeP.views.home', name='home'),
    # url(r'^SiGeP/', include('SiGeP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
     url(r'^',include('RecursosDeEmpresa.urls')),
     url(r'^',include('ConfiguracionDeComponentes.urls')),
     url(r'^',include('PedidoRegistrado.urls')),
     url(r'^',include('ComponentesDePedido.urls')),
     #Registration URLS
     url(r'accounts/register/$', 
        RegistrationView.as_view(form_class = ExRegistrationForm), 
        name = 'registration_register'),
 
     url(r'^accounts/', include('registration.backends.default.urls')),
     
     url(r'^chaining/', include('smart_selects.urls')),
)
