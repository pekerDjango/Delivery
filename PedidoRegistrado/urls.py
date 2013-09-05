from django.conf.urls import patterns,url


urlpatterns = patterns('PedidoRegistrado.views',    
     url(r'^pedido/$','pedidoInformacion_view',name='vista_pedidoInformacion'),
     url(r'^pedido/armaTuPedido/$','armaTuPedido_view',name='vista_armaTuPedido'),

)   
