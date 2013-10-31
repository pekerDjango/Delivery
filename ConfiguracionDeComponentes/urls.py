from django.conf.urls import patterns,url

urlpatterns = patterns('ConfiguracionDeComponentes.views',
    url(r'^$','index_view',name='vista_index'),
)   

