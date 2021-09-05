#define os padrões de url

from django.conf.urls import url

from . import views

urlpatterns = [
    #página inicial
    url(r'^$', views.index, name='index'),
    #página para listar assuntos
    url(r'^topics/$', views.index, name='topics'),
    #página para listar as entradas sobre um assunto
    url(r'^topics/(?P<topic_id>\d+)/$', views.index, name='topic'),
    #página para crair um novo assunto
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]