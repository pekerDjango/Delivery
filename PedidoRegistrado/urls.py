from django.conf.urls import patterns,url


urlpatterns = patterns('PedidoRegistrado.views',    
     url(r'^pedido/$','pedidoInformacion_view',name='vista_pedidoInformacion'),
     url(r'^pedido/armaTuPedido/$','armaTuPedido_view',name='vista_armaTuPedido'),
     url(r'^pedido/armaTuPedido/productosSolicitados/(?P<codigo>.*)/$','productosSolicitados_view',name='vista_productosSolicitados'),
     url(r'^pedido/armaTuPedido/menusDisponibles/$','menuDisponibles_view',name='vista_menuDisponibles'),
     url(r'^pedido/armaTuPedido/promosDisponibles/$','promocionDisponibles_view',name='vista_promosDisponibles'),
     url(r'^pedido/armaTuPedido/productosPopulares/$','productosPopulares_view',name='vista_productosPopulares'),



)   
