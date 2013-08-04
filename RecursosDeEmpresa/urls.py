from django.conf.urls import patterns,url


urlpatterns = patterns('RecursosDeEmpresa.views',
     url(r'^tipos/page/(?P<pagina>.*)/$','tipoDocumento_view',name='vista_tipo'),
     url(r'^indexAdmin/$','indexAdmin_view',name='vista_indexAdmin'),
     url(r'^recursosDeEmpresa/empleados/page/(?P<pagina>.*)/$','empleado_view',name='vista_empleado'),
     url(r'^add/empleado/$','add_empleado_view', name='vista_agregar_empleado'),
)   
