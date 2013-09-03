from django.conf.urls import patterns,url

urlpatterns = patterns('ConfiguracionDeComponentes.views',
    url(r'^$','index_view',name='vista_index'),
    url(r'^login/$','login_view',name='vista_login'),    
    url(r'^logout/$','logout_view',name='vista_logout'),
)   

