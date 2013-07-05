# coding: utf-8
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Galeria, Autor, Sugestao


class AutorListView(ListView):
    queryset = Autor.objects.ativos()
    context_object_name = 'autores'
    template_name = 'autores.html'


class AutorDetailView(DetailView):
    model = Autor
    context_object_name = 'autor'
    template_name = 'autor.html'


class GaleriaListView(ListView):
    queryset = Galeria.objects.ativos()
    context_object_name = 'quadros'
    template_name = 'galeria.html'


class SugestaoListView(ListView):
    queryset = Sugestao.objects.ativos()
    context_object_name = 'sugestoes'
    template_name = 'sugestoes.html'


class VenderTemplateView(TemplateView):
    template_name = 'vender.html'


class ComprarTemplateView(TemplateView):
    template_name = 'comprar.html'


class ContatoTemplateView(TemplateView):
    template_name = 'contato.html'
