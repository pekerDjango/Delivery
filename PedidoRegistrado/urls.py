from django.conf.urls import patterns,url


urlpatterns = patterns('PedidoRegistrado.views',    
     url(r'^pedido/$','pedidoInformacion_view',name='vista_pedidoInformacion'),
     url(r'^pedido/armaTuPedido/$','armaTuPedido_view',name='vista_armaTuPedido'),
     url(r'^pedido/armaTuPedido/productosSolicitados/(?P<codigo>.*)/$','productosSolicitados_view',name='vista_productosSolicitados'),
     url(r'^pedido/armaTuPedido/menusDisponibles/$','menuDisponibles_view',name='vista_menuDisponibles'),
     url(r'^pedido/armaTuPedido/promosDisponibles/$','promocionDisponibles_view',name='vista_promosDisponibles'),
     url(r'^pedido/armaTuPedido/productosPopu/$','productosPopulares_view',name='vista_productosPopulares'),
     url(r'^pedido/armaTuPedido/productosPopulares/(?P<cantidad>.*)/(?P<id_pro>.*)/$','agregarPedido_view',name='vista_agregarProducto'),
     url(r'^pedido/armaTuPedido/detallePedido/$','detallePedido_view',name='vista_detallePedido'),
     url(r'^pedido/armaTuPedido/detallePedido/detallePago/$','detallePago_view',name='vista_detallePago'),
     url(r'^pedido/armaTuPedido/detallePedido/detallePago/pedidoFinalizado/$','pedidoFinalizado_view',name='vista_pedidoFinalizado'),
     url(r'^$','cerrarPedido_view',name='vista_cerrarPedido'),  


)   
