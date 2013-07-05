# coding: utf-8
from django.conf.urls import patterns, url
from .views import GaleriaListView, AutorListView, AutorDetailView, SugestaoListView, ContatoTemplateView

urlpatterns = patterns('',
    url(r'^$', GaleriaListView.as_view(), name='home'),
    url(r'^autores/$', AutorListView.as_view(), name='autores'),
    url(r'^autor/(?P<pk>\d+)/$', AutorDetailView.as_view(), name='autor'),
    url(r'^sugestoes/$', SugestaoListView.as_view(), name='sugestoes'),
    url(r'^contato/$', ContatoTemplateView.as_view(), name='contato'),
)
