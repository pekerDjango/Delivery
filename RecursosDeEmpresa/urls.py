from django.conf.urls import patterns,url


urlpatterns = patterns('RecursosDeEmpresa.views',    
     url(r'^indexAdmin/$','indexAdmin_view',name='vista_indexAdmin'),
     url(r'^recursosDeEmpresa/empleados/page/(?P<pagina>.*)/$','empleado_view',name='vista_empleado'),
     url(r'^add/empleado/$','add_empleado_view', name='vista_agregar_empleado'),
     url(r'^edit/empleado/(?P<id_emp>.*)/$','edit_empleado_view', name= "vista_editar_empleado"),
     url(r'^empleado/(?P<id_emp>.*)/$','singleEmpleado_view',name='vista_single_empleado'),
     url(r'^delete/empleado/(?P<id_emp>.*)/$','delete_empleado_view', name= "vista_editar_empleado"),
     url(r'^sucursales/$','sucursal_view',name='vista_sucursal'),
)   