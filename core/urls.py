# coding: utf-8
from django.conf.urls import patterns, url
from .views import (HomeListView, GaleriaListView, AutorListView, AutorDetailView, SugestaoListView, ContatoTemplateView,
                    ComprarTemplateView, VenderTemplateView, GalleryRoomListView)

urlpatterns = patterns('',
    url(r'^$', HomeListView.as_view(), name='home'),
    url(r'^gallery/$', GalleryRoomListView.as_view(), name='gallery'),
    url(r'^galeria/$', GaleriaListView.as_view(), name='galeria'),
    url(r'^autores/$', AutorListView.as_view(), name='autores'),
    url(r'^autor/(?P<pk>\d+)/$', AutorDetailView.as_view(), name='autor'),
    url(r'^sugestoes/$', SugestaoListView.as_view(), name='sugestoes'),
    url(r'^vender/$', VenderTemplateView.as_view(), name='vender'),
    url(r'^comprar/$', ComprarTemplateView.as_view(), name='comprar'),
    url(r'^contato/$', ContatoTemplateView.as_view(), name='contato'),
)
