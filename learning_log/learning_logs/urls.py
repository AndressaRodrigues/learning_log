#define os padrões de url

from django.conf.urls import url

from . import views

urlpatterns = [
    #página inicial
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.index, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.index, name='topic'),
]