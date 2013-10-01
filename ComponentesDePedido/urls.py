from django.conf.urls import patterns,url


urlpatterns = patterns('ComponentesDePedido.views',    
     url(r'^producto/$','productoListado_view',name='vista_producto_listado'),

)   
