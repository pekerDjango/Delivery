from django.conf.urls import patterns,url


urlpatterns = patterns('RecursosDeEmpresa.views',
     url(r'^tipos/page/(?P<pagina>.*)/$','tipoDocumento_view',name='vista_tipo'),
     url(r'^indexAdmin/$','indexAdmin_view',name='vista_about'),
)   
