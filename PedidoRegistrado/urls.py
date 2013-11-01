from django.conf.urls import patterns,url


urlpatterns = patterns('PedidoRegistrado.views',    
     url(r'^pedido/$','pedidoInformacion_view',name='vista_pedidoInformacion'),
     url(r'^pedido/actualizar/(?P<id_dom>.*)/$','actualizarPedidoInformacion_view',name='vista_actualizarPedidoInformacion'),
     url(r'^pedido/armaTuPedido/$','armaTuPedido_view',name='vista_armaTuPedido'),
     url(r'^pedido/armaTuPedido/productosSolicitados/(?P<codigo>.*)/$','productosSolicitados_view',name='vista_productosSolicitados'),
     url(r'^pedido/armaTuPedido/menusDisponibles/$','menuDisponibles_view',name='vista_menuDisponibles'),
     url(r'^pedido/armaTuPedido/del/productos/(?P<id_det>.*)$','eliminarDetalle_view',name='vista_eliminarDetalle'),
     url(r'^pedido/armaTuPedido/promosDisponibles/$','promocionDisponibles_view',name='vista_promosDisponibles'),
     url(r'^pedido/armaTuPedido/productosPopu/$','productosPopulares_view',name='vista_productosPopulares'),
     url(r'^pedido/armaTuPedido/productos/(?P<cantidad>.*)/(?P<id_pro>.*)/(?P<id_tip>.*)/$','agregarPedido_view',name='vista_agregarProducto'),
     url(r'^pedido/armaTuPedido/productosActualizar/(?P<nueva_cantidad>.*)/(?P<id_det>.*)/$','actualizar_detalle_pedido_view', name = 'vista_actualizarProducto'),
     url(r'^pedido/armaTuPedido/detallePedido/$','detallePedido_view',name='vista_detallePedido'),
     url(r'^pedido/armaTuPedido/detallePedido/detallePago/$','detallePago_view',name='vista_detallePago'),
     url(r'^pedido/armaTuPedido/detallePedido/detallePago/pedidoFinalizado/$','pedidoFinalizado_view',name='vista_pedidoFinalizado'),
     url(r'^$','cerrarPedido_view',name='vista_cerrarPedido'),
     url(r'^pedido/armaTuPedido/productoParaArmar/(?P<id_pro>.*)/$','productoParaArmar_view',name='vista_productoParaArmar'),
     url(r'^pedido/sucursales/$','sucursales_view',name='vista_sucursales'),
     url(r'^pedido/sucursales/elegir/(?P<id_suc>.*)/$','sucursalElegir_view',name='vista_sucursalElegida'),
     url(r'^pedido/armaTuPedido/productoArmado/(?P<id_ver>.*)/$','productoArmado_view',name='vista_productoArmado'),
     url(r'^pedido/armaTuPedido/addIngrediente/productoArmado/(?P<id_ing>.*)/$','productoArmadoIngrediente_view',name='vista_productoArmadoIngrediente'),
     url(r'^getTuProducto/$','tuProducto_view',name= "get_tuProducto"),
     url(r'^pedido/armaTuPedido/guardarProducto$','guardarProducto_view',name='vista_guardarProducto'),


)   
